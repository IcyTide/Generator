from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSplitter, QVBoxLayout, QWidget)

from qt.classes.kungfu import DisplayKungfu
from qt.classes.section import Section
from qt import LabelRow, Table


class LoopWidget(QWidget):
    kungfu: DisplayKungfu
    sections: list[Section]

    @property
    def section(self):
        section_index = self.section_table.currentRow()
        if section_index < 0:
            return None
        return self.sections[section_index]

    @property
    def records(self):
        if not (section := self.section):
            return []
        return section.records

    @property
    def record(self):
        record_index = self.record_table.currentRow()
        if record_index < 0:
            return None
        return self.records[record_index]

    def __init__(self):
        super().__init__()
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left Panel - Sections and Records
        left_layout = QVBoxLayout((left_panel := QWidget()))

        # Section Display
        self.section_table = Table(["ID", "Name", "Count"])
        self.sections = []
        self.section_label = QLabel("")
        left_layout.addWidget(LabelRow("Current Section:", self.section_label))
        left_layout.addWidget(self.section_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_section_btn = QPushButton("Add Section")
        btn_layout.addWidget(self.add_section_btn)
        self.copy_section_btn = QPushButton("Copy Section")
        btn_layout.addWidget(self.copy_section_btn)
        self.del_section_btn = QPushButton("Delete Section")
        btn_layout.addWidget(self.del_section_btn)

        # Record Display
        self.record_label = QLabel("")
        left_layout.addWidget(LabelRow("Current Record:", self.record_label))
        self.record_table = Table(["ID", "Name", "Count"])
        left_layout.addWidget(self.record_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_record_btn = QPushButton("Add Record")
        btn_layout.addWidget(self.add_record_btn)
        self.copy_record_btn = QPushButton("Copy Record")
        btn_layout.addWidget(self.copy_record_btn)
        self.del_record_btn = QPushButton("Delete Record")
        btn_layout.addWidget(self.del_record_btn)

        # Right Panel - Buff and Skill and Dot
        right_layout = QVBoxLayout((right_panel := QWidget()))

        # Buff Display
        right_layout.addWidget(QLabel("Buff List"))
        self.buff_table = Table(["Name", "ID", "Level", "Stack", "Type"])
        right_layout.addWidget(self.buff_table)
        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_buff_btn = QPushButton("Add Buff")
        btn_layout.addWidget(self.add_buff_btn)
        self.copy_buff_btn = QPushButton("Copy Buff")
        btn_layout.addWidget(self.copy_buff_btn)
        self.del_buff_btn = QPushButton("Delete Buff")
        btn_layout.addWidget(self.del_buff_btn)

        # Skill Display
        right_layout.addWidget(QLabel("Skill List"))
        self.skill_table = Table(["Name", "ID", "Level", "Count"])
        right_layout.addWidget(self.skill_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_skill_btn = QPushButton("Add Skill")
        btn_layout.addWidget(self.add_skill_btn)
        self.copy_skill_btn = QPushButton("Copy Skill")
        btn_layout.addWidget(self.copy_skill_btn)
        self.del_skill_btn = QPushButton("Delete Skill")
        btn_layout.addWidget(self.del_skill_btn)

        # Dot Display
        right_layout.addWidget(QLabel("Dot List"))
        self.dot_table = Table(["Name", "ID", "Level", "Source", "Tick", "Count"])
        right_layout.addWidget(self.dot_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_dot_btn = QPushButton("Add Dot")
        btn_layout.addWidget(self.add_dot_btn)
        self.copy_dot_btn = QPushButton("Copy Dot")
        btn_layout.addWidget(self.copy_dot_btn)
        self.del_dot_btn = QPushButton("Delete Dot")
        btn_layout.addWidget(self.del_dot_btn)

        # Main Widget Set
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(right_panel)
        layout = QVBoxLayout(self)
        layout.addWidget(main_splitter)
