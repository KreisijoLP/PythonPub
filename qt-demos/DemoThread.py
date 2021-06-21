#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import threading

from PyQt5.QtCore import QTimer, QObject, pyqtSignal, \
     QThread, Qt

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem,
    QPushButton,
    QVBoxLayout,
)

TASKNUMBER = 460


class Worker(QObject):
    generated_item = pyqtSignal(str)
    work_started = pyqtSignal()
    work_done = pyqtSignal()

    def work(self):
        self.work_started.emit()
        for i in range(TASKNUMBER):
            for _ in range(1000000):  # just burn some time
                pass
            self.generated_item.emit("Item {}".format(i))
        self.work_done.emit()


class TimeMeasurer(QObject):

    def start(self):
        self._start = time.monotonic()

    def stop(self):
        elapsed = time.monotonic() - self._start
        print("Time elapsed:", elapsed)


class Forwarder(QObject):
    """
    Just a holder for one signal
    """
    enqueue_work = pyqtSignal()


class BatchCounter(QObject):

    count_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._lock = threading.Lock()
        self._count = 0

    def inc(self):
        with self._lock:
            self._count += 1
        self.count_changed.emit(self._count)


    def dec(self):
        with self._lock:
            self._count -= 1
        self.count_changed.emit(self._count)


def main():
    forwarder = Forwarder()
    counter = BatchCounter()

    extra_threads = []

    def generate_work_load():
        counter.inc()
        forwarder.enqueue_work.emit()

    def generate_work_load_in_extra_thread():
        def shutdown_thread():
            print("running threads:", len(extra_threads))
            extra_thread.quit()
            extra_thread.wait()
            extra_threads.remove(extra_thread)
            print("shutdown_thread")

        extra_thread = QThread()
        worker = extra_thread.worker = Worker()
        worker.moveToThread(worker_thread)

        extra_thread.started.connect(worker.work)
        tm = extra_thread.tm = TimeMeasurer()

        worker.generated_item.connect(add_item)
        worker.work_started.connect(tm.start)
        worker.work_done.connect(tm.stop)
        worker.work_done.connect(counter.dec)
        worker.work_done.connect(shutdown_thread)
        extra_threads.append(extra_thread)
        counter.inc()
        extra_thread.start()


    app = QApplication(sys.argv)

    worker_thread = QThread()
    worker = Worker()
    worker.moveToThread(worker_thread)

    w = QWidget()
    w.setWindowTitle('ThreadTest')

    layout = QVBoxLayout(w)
    start_in_worker_thread_button = QPushButton(w)
    start_in_worker_thread_button.setText("Add Items in Worker Thread")
    start_in_worker_thread_button.clicked.connect(generate_work_load)

    start_in_extra_thread_button = QPushButton(w)
    start_in_extra_thread_button.setText("Add Items in Extra Thread")
    start_in_extra_thread_button.clicked.connect(generate_work_load_in_extra_thread)

    counting_label = QLabel(w)
    counter.count_changed.connect(lambda count: counting_label.setText("Batches: {}".format(count)))

    tree = QTreeWidget(w)

    layout.addWidget(start_in_worker_thread_button)
    layout.addWidget(start_in_extra_thread_button)
    layout.addWidget(counting_label)
    layout.addWidget(tree)

    def add_item(text):
        parent = QTreeWidgetItem(tree)
        tree.addTopLevelItem(parent)
        parent.setText(0, text)

    w.show()

    tm = TimeMeasurer()

    worker.generated_item.connect(add_item)
    worker.work_started.connect(tm.start)
    worker.work_done.connect(tm.stop)
    worker.work_done.connect(counter.dec)
    forwarder.enqueue_work.connect(worker.work)

    # the ONE background thread
    worker_thread.start()

    app.exec_()
    worker_thread.quit()
    worker_thread.wait()
    sys.exit()

if __name__ == '__main__':
    main()
