import sys
from typing import List

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTableWidgetItem,
    QPushButton, QLabel, QDialog, QSplitter
)
from PySide6.QtCore import Qt

from base.buff import Buff
from base.section import Section
from base.skill import Skill
from base.dot import Dot
from qt import LabelRow, Table
from qt.component.buff_editor import BuffEditorDialog
from qt.component.dot_editor import DotEditorDialog
from qt.component.record_editor import RecordEditorDialog
from qt.component.section_editor import SectionEditorDialog
from qt.component.skill_editor import SkillEditorDialog


class MainWindow(QMainWindow):
    sections: List[Section]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.icon = QIcon("assets/icon.ico")
        self.setWindowIcon(self.icon)
        self.setGeometry(100, 100, 1000, 600)

        # 主体布局
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left Panel - Sections and Records
        left_layout = QVBoxLayout((left_panel := QWidget()))

        # Section Display
        self.sections = [Section()]
        self.section_label = QLabel(self.sections[0].name)
        left_layout.addWidget(LabelRow("Current Section:", self.section_label))
        self.section_table = Table(["ID", "Name", "Count"])
        left_layout.addWidget(self.section_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((add_section_btn := QPushButton("Add Section")))
        btn_layout.addWidget((del_section_btn := QPushButton("Delete Section")))

        # Record Display
        self.record_label = QLabel("")
        left_layout.addWidget(LabelRow("Current Record:", self.record_label))
        self.record_table = Table(["ID", "Name", "Count"])
        left_layout.addWidget(self.record_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((add_record_btn := QPushButton("Add Record")))
        btn_layout.addWidget((del_record_btn := QPushButton("Delete Record")))

        # Right Panel - Buff and Skill and Dot
        right_layout = QVBoxLayout((right_panel := QWidget()))

        # Buff Display
        right_layout.addWidget(QLabel("Buff List"))
        self.buff_table = Table(["Type", "ID", "Level", "Stack"])
        right_layout.addWidget(self.buff_table)
        right_layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((add_buff_btn := QPushButton("Add Buff")))
        btn_layout.addWidget((del_buff_btn := QPushButton("Delete Buff")))

        # Skill Display
        right_layout.addWidget(QLabel("Skill List"))
        self.skill_table = Table(["ID", "Level", "Count"])
        right_layout.addWidget(self.skill_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((add_skill_btn := QPushButton("Add Skill")))
        btn_layout.addWidget((del_skill_btn := QPushButton("Delete Skill")))

        # Dot Display
        right_layout.addWidget(QLabel("Dot List"))
        self.dot_table = Table(["ID", "Level", "Source", "Consume", "Count"])
        right_layout.addWidget(self.dot_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        btn_layout.addWidget((add_dot_btn := QPushButton("Add Dot")))
        btn_layout.addWidget((del_dot_btn := QPushButton("Delete Dot")))

        # Connect Slot
        add_section_btn.clicked.connect(self.add_section)
        self.section_table.itemClicked.connect(self.select_section)
        self.section_table.itemDoubleClicked.connect(self.edit_section)
        del_section_btn.clicked.connect(self.delete_section)

        add_record_btn.clicked.connect(self.add_record)
        self.record_table.itemClicked.connect(self.select_record)
        self.record_table.itemDoubleClicked.connect(self.edit_record)
        del_record_btn.clicked.connect(self.delete_record)

        add_buff_btn.clicked.connect(self.add_buff)
        self.buff_table.itemDoubleClicked.connect(self.edit_buff)
        del_buff_btn.clicked.connect(self.delete_buff)

        add_skill_btn.clicked.connect(self.add_skill)
        self.skill_table.itemDoubleClicked.connect(self.edit_skill)
        del_skill_btn.clicked.connect(self.delete_skill)

        add_dot_btn.clicked.connect(self.add_dot)
        self.dot_table.itemDoubleClicked.connect(self.edit_dot)
        del_dot_btn.clicked.connect(self.delete_dot)

        # Main Widget Set
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(right_panel)
        self.setCentralWidget(main_splitter)

        self.refresh_table(self.section_table, self.sections, True)
        self.select_section()


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

    @staticmethod
    def refresh_table(table, table_data, index=False):
        table.setRowCount(0)
        for i, row in enumerate(table_data):
            table.insertRow(i)
            if index:
                table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            for j, data in enumerate(row):
                table.setItem(i, j + int(index), QTableWidgetItem(data))
        table.setCurrentCell(len(table_data) - 1, 0)

    def select_section(self):
        if not (section := self.section):
            return
        self.section_label.setText(section.name)
        self.refresh_table(self.record_table, self.records, True)
        self.select_record()

    def add_section(self):
        dialog = SectionEditorDialog(parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections.append(dialog.section)
            self.refresh_table(self.section_table, self.sections, True)
            self.select_section()

    def edit_section(self):
        if not (section := self.section):
            return
        dialog = SectionEditorDialog(section, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections[self.section_table.currentRow()] = dialog.section
            self.refresh_table(self.section_table, self.sections, True)
            self.section_label.setText(dialog.section.name)

    def delete_section(self):
        if not (section := self.section):
            return
        self.sections.remove(section)
        self.refresh_table(self.section_table, self.sections, True)
        self.select_section()

    def select_record(self):
        if not (record := self.record):
            return
        self.record_label.setText(record.name)
        self.refresh_table(self.buff_table, self.record.buffs)
        self.refresh_table(self.skill_table, self.record.skills)
        self.refresh_table(self.dot_table, self.record.dots)

    def add_record(self):
        dialog = RecordEditorDialog(parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.records.append(dialog.record)
            self.refresh_table(self.record_table, self.records, True)
            self.select_record()

    def edit_record(self):
        if not (record := self.record):
            return
        dialog = RecordEditorDialog(record, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.name = dialog.record.name
            record.count = dialog.record.count
            self.refresh_table(self.record_table, self.records, True)
            self.record_label.setText(record.name)

    def delete_record(self):
        if not (record := self.record):
            return
        self.records.remove(record)
        self.refresh_table(self.record_table, self.records, True)
        self.select_record()

    def add_buff(self):
        if not (record := self.record):
            return
        dialog = BuffEditorDialog(items=[123, 456], parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (buff := dialog.buff):
            record.buffs.append(buff)
            self.refresh_table(self.buff_table, record.buffs)

    def edit_buff(self):
        if not (record := self.record):
            return
        buff_index = self.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        dialog = BuffEditorDialog(value=buff, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.buffs[buff_index] = dialog.buff
            self.refresh_table(self.buff_table, record.buffs)

    def delete_buff(self):
        if not (record := self.record):
            return
        buff_index = self.buff_table.currentRow()
        if buff_index < 0:
            return
        del record.buffs[buff_index]
        self.refresh_table(self.buff_table, record.buffs)

    def add_skill(self):
        if not (record := self.record):
            return
        dialog = SkillEditorDialog(items=[321, 654], parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            record.skills.append(skill)
            self.refresh_table(self.skill_table, record.skills)

    def edit_skill(self):
        if not (record := self.record):
            return
        skill_index = self.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        dialog = SkillEditorDialog(value=skill, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.skills[skill_index] = dialog.skill
            self.refresh_table(self.skill_table, record.skills)

    def delete_skill(self):
        if not (record := self.record):
            return
        skill_index = self.skill_table.currentRow()
        if skill_index < 0:
            return
        del record.skills[skill_index]
        self.refresh_table(self.skill_table, record.skills)

    def add_dot(self):
        if not (record := self.record):
            return
        dialog = DotEditorDialog(items=[987, 654], parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (dot := dialog.dot):
            record.dots.append(dot)
            self.refresh_table(self.dot_table, record.dots)

    def edit_dot(self):
        if not (record := self.record):
            return
        dot_index = self.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dialog = DotEditorDialog(value=dot, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.dots[dot_index] = dialog.dot
            self.refresh_table(self.dot_table, record.dots)

    def delete_dot(self):
        if not (record := self.record):
            return
        dot_index = self.dot_table.currentRow()
        if dot_index < 0:
            return
        del record.dots[dot_index]
        self.refresh_table(self.dot_table, record.dots)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
