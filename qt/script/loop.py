from copy import deepcopy

from PySide6.QtWidgets import QDialog, QTableWidgetItem

from base.section import Section
from qt.component.loop_widget.buff_editor import BuffEditorDialog
from qt.component.loop_widget.dot_editor import DotEditorDialog
from qt.component.loop_widget.record_editor import RecordEditorDialog
from qt.component.loop_widget.section_editor import SectionEditorDialog
from qt.component.loop_widget.skill_editor import SkillEditorDialog
from qt.component.loop_widget.widget import LoopWidget


def refresh_table(table, table_data, index=False):
    table.setRowCount(0)
    for i, row in enumerate(table_data):
        table.insertRow(i)
        if index:
            table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
        for j, data in enumerate(row):
            table.setItem(i, j + int(index), QTableWidgetItem(data))
    table.setCurrentCell(len(table_data) - 1, 0)


def loop_script(self: LoopWidget):
    def select_section():
        if not (section := self.section):
            return
        self.section_label.setText(section.name)
        refresh_table(self.record_table, self.records, True)
        select_record()

    def add_section():
        dialog = SectionEditorDialog(parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections.append(dialog.section)
            refresh_table(self.section_table, self.sections, True)
            select_section()

    def edit_section():
        if not (section := self.section):
            return
        dialog = SectionEditorDialog(section, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections[self.section_table.currentRow()] = dialog.section
            refresh_table(self.section_table, self.sections, True)
            self.section_label.setText(dialog.section.name)

    def copy_section():
        if not (section := self.section):
            return
        section_copy = deepcopy(section)
        section_copy.name = f"{section_copy.name} - Copy"
        self.sections.append(section_copy)
        refresh_table(self.section_table, self.sections, True)
        self.section_table.selectRow(len(self.sections) - 1)
        self.section_label.setText(section_copy.name)

    def delete_section():
        if not (section := self.section):
            return
        self.sections.remove(section)
        refresh_table(self.section_table, self.sections, True)
        select_section()

    self.add_section_btn.clicked.connect(add_section)
    self.section_table.itemClicked.connect(select_section)
    self.section_table.itemDoubleClicked.connect(edit_section)
    self.copy_section_btn.clicked.connect(copy_section)
    self.del_section_btn.clicked.connect(delete_section)

    def select_record():
        if not (record := self.record):
            return
        self.record_label.setText(record.name)
        refresh_table(self.buff_table, self.record.buffs)
        refresh_table(self.skill_table, self.record.skills)
        refresh_table(self.dot_table, self.record.dots)

    def add_record():
        dialog = RecordEditorDialog(parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.records.append(dialog.record)
            refresh_table(self.record_table, self.records, True)
            select_record()

    def edit_record():
        if not (record := self.record):
            return
        dialog = RecordEditorDialog(record, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.name = dialog.record.name
            record.count = dialog.record.count
            refresh_table(self.record_table, self.records, True)
            self.record_label.setText(record.name)

    def copy_record():
        if not (record := self.record):
            return
        record_copy = deepcopy(record)
        record_copy.name = f"{record_copy.name} - Copy"
        self.records.append(record_copy)
        refresh_table(self.record_table, self.records, True)
        self.record_table.selectRow(len(self.records) - 1)
        self.record_label.setText(record_copy.name)

    def delete_record():
        if not (record := self.record):
            return
        self.records.remove(record)
        refresh_table(self.record_table, self.records, True)
        select_record()

    self.add_record_btn.clicked.connect(add_record)
    self.record_table.itemClicked.connect(select_record)
    self.record_table.itemDoubleClicked.connect(edit_record)
    self.copy_record_btn.clicked.connect(copy_record)
    self.del_record_btn.clicked.connect(delete_record)

    def add_buff():
        if not (record := self.record):
            return
        dialog = BuffEditorDialog(buffs=self.kungfu.buffs, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (buff := dialog.buff):
            record.buffs.append(buff)
            refresh_table(self.buff_table, record.buffs)

    def edit_buff():
        if not (record := self.record):
            return
        buff_index = self.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        dialog = BuffEditorDialog(buffs=self.kungfu.buffs, buff=buff, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.buffs[buff_index] = dialog.buff
            refresh_table(self.buff_table, record.buffs)

    def copy_buff():
        if not (record := self.record):
            return
        buff_index = self.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        buff_copy = deepcopy(buff)
        buff_copy.name = f"{buff_copy.name} - Copy"
        record.buffs.append(buff_copy)
        refresh_table(self.buff_table, record.buffs)

    def delete_buff():
        if not (record := self.record):
            return
        buff_index = self.buff_table.currentRow()
        if buff_index < 0:
            return
        del record.buffs[buff_index]
        refresh_table(self.buff_table, record.buffs)

    self.add_buff_btn.clicked.connect(add_buff)
    self.buff_table.itemDoubleClicked.connect(edit_buff)
    self.copy_buff_btn.clicked.connect(copy_buff)
    self.del_buff_btn.clicked.connect(delete_buff)

    def add_skill():
        if not (record := self.record):
            return
        dialog = SkillEditorDialog(skills=self.kungfu.skills, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            record.skills.append(skill)
            refresh_table(self.skill_table, record.skills)

    def edit_skill():
        if not (record := self.record):
            return
        skill_index = self.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        dialog = SkillEditorDialog(skills=self.kungfu.skills, skill=skill, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.skills[skill_index] = dialog.skill
            refresh_table(self.skill_table, record.skills)

    def copy_skill():
        if not (record := self.record):
            return
        skill_index = self.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        skill_copy = deepcopy(skill)
        skill_copy.name = f"{skill_copy.name} - Copy"
        record.skills.append(skill_copy)
        refresh_table(self.skill_table, record.skills)

    def delete_skill():
        if not (record := self.record):
            return
        skill_index = self.skill_table.currentRow()
        if skill_index < 0:
            return
        del record.skills[skill_index]
        refresh_table(self.skill_table, record.skills)

    self.add_skill_btn.clicked.connect(add_skill)
    self.skill_table.itemDoubleClicked.connect(edit_skill)
    self.copy_skill_btn.clicked.connect(copy_skill)
    self.del_skill_btn.clicked.connect(delete_skill)

    def add_dot():
        if not (record := self.record):
            return
        dialog = DotEditorDialog(dots=self.kungfu.dots, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted and (dot := dialog.dot):
            record.dots.append(dot)
            refresh_table(self.dot_table, record.dots)

    def edit_dot():
        if not (record := self.record):
            return
        dot_index = self.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dialog = DotEditorDialog(dots=self.kungfu.dots, dot=dot, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.dots[dot_index] = dialog.dot
            refresh_table(self.dot_table, record.dots)

    def copy_dot():
        if not (record := self.record):
            return
        dot_index = self.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dot_copy = deepcopy(dot)
        dot_copy.name = f"{dot_copy.name} - Copy"
        record.dots.append(dot_copy)
        refresh_table(self.dot_table, record.dots)

    def delete_dot():
        if not (record := self.record):
            return
        dot_index = self.dot_table.currentRow()
        if dot_index < 0:
            return
        del record.dots[dot_index]
        refresh_table(self.dot_table, record.dots)

    self.add_dot_btn.clicked.connect(add_dot)
    self.dot_table.itemDoubleClicked.connect(edit_dot)
    self.copy_dot_btn.clicked.connect(copy_dot)
    self.del_dot_btn.clicked.connect(delete_dot)

    def init_loop(sections: list = None):
        if sections:
            self.sections = sections
        else:
            self.sections = [Section()]
        refresh_table(self.section_table, self.sections, True)
        select_section()
        return self.sections

    self.init_loop = init_loop
    init_loop()