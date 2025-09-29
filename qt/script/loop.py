from copy import deepcopy

from PySide6.QtWidgets import QDialog, QTableWidgetItem

from qt.classes.attribute import Attribute
from qt.classes.buff import BuffType
from qt.classes.section import Section
from qt.component.loop_widget.buff_dialog import BuffEditorDialog
from qt.component.loop_widget.dot_dialog import DotDamageDialog, DotEditorDialog
from qt.component.loop_widget.record_dialog import RecordEditorDialog
from qt.component.loop_widget.section_dialog import SectionEditorDialog
from qt.component.loop_widget.skill_dialog import SkillDamageDialog
from qt.component.loop_widget.skill_dialog import SkillEditorDialog
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


class LoopScript:
    def __init__(self, loop_widget: LoopWidget):
        self.widget = loop_widget

        self.connect()

    def connect(self):
        self.widget.skill_damage_btn.clicked.connect(self.cal_skill_damage)
        self.widget.dot_damage_btn.clicked.connect(self.cal_dot_damage)

        self.widget.section_table.itemClicked.connect(self.select_section)
        self.widget.add_section_btn.clicked.connect(self.add_section)
        self.widget.section_table.itemDoubleClicked.connect(self.edit_section)
        self.widget.copy_section_btn.clicked.connect(self.copy_section)
        self.widget.del_section_btn.clicked.connect(self.delete_section)

        self.widget.record_table.itemClicked.connect(self.select_record)
        self.widget.add_record_btn.clicked.connect(self.add_record)
        self.widget.record_table.itemDoubleClicked.connect(self.edit_record)
        self.widget.copy_record_btn.clicked.connect(self.copy_record)
        self.widget.del_record_btn.clicked.connect(self.delete_record)

        self.widget.add_buff_btn.clicked.connect(self.add_buff)
        self.widget.buff_table.itemDoubleClicked.connect(self.edit_buff)
        self.widget.copy_buff_btn.clicked.connect(self.copy_buff)
        self.widget.del_buff_btn.clicked.connect(self.delete_buff)

        self.widget.skill_table.itemClicked.connect(self.select_skill)
        self.widget.add_skill_btn.clicked.connect(self.add_skill)
        self.widget.skill_table.itemDoubleClicked.connect(self.edit_skill)
        self.widget.copy_skill_btn.clicked.connect(self.copy_skill)
        self.widget.del_skill_btn.clicked.connect(self.delete_skill)

        self.widget.dot_table.itemClicked.connect(self.select_dot)
        self.widget.add_dot_btn.clicked.connect(self.add_dot)
        self.widget.dot_table.itemDoubleClicked.connect(self.edit_dot)
        self.widget.copy_dot_btn.clicked.connect(self.copy_dot)
        self.widget.del_dot_btn.clicked.connect(self.delete_dot)

    def add_buff_to_attribute(self, attribute: Attribute, buff_type: BuffType):
        buffs = self.widget.record.buffs
        for buff in buffs:
            if buff.buff_type == buff_type:
                attribute.add_buff(buff)

    def cal_skill_damage(self):
        if not (record := self.widget.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        attribute = self.widget.kungfu.create_attribute()
        self.add_buff_to_attribute(attribute, BuffType.Current)
        SkillDamageDialog(skill, attribute, parent=self.widget).exec()

    def cal_dot_damage(self):
        if not (record := self.widget.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
             return
        dot = record.dots[dot_index]
        current_attribute = self.widget.kungfu.create_attribute()
        self.add_buff_to_attribute(current_attribute, BuffType.Current)
        snapshot_attribute = self.widget.kungfu.create_attribute()
        self.add_buff_to_attribute(snapshot_attribute, BuffType.Snapshot)
        DotDamageDialog(dot, current_attribute, snapshot_attribute, parent=self.widget).exec()

    def show_skill_damage_btn(self):
        self.widget.skill_damage_btn.show()
        self.widget.dot_damage_btn.hide()

    def show_dot_damage_btn(self):
        self.widget.skill_damage_btn.hide()
        self.widget.dot_damage_btn.show()

    def select_section(self):
        if not (section := self.widget.section):
            return
        self.widget.section_label.setText(section.name)
        refresh_table(self.widget.record_table, self.widget.records, True)
        self.select_record()

    def add_section(self):
        dialog = SectionEditorDialog(parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.widget.sections[self.widget.section_table.currentRow()] = dialog.section
            refresh_table(self.widget.section_table, self.widget.sections, True)
            self.widget.section_label.setText(dialog.section.name)

    def edit_section(self):
        if not (section := self.widget.section):
            return
        dialog = SectionEditorDialog(section, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.widget.sections[self.widget.section_table.currentRow()] = dialog.section
            refresh_table(self.widget.section_table, self.widget.sections, True)
            self.widget.section_label.setText(dialog.section.name)

    def copy_section(self):
        if not (section := self.widget.section):
            return
        section_copy = deepcopy(section)
        section_copy.name = f"{section_copy.name} - Copy"
        self.widget.sections.append(section_copy)
        refresh_table(self.widget.section_table, self.widget.sections, True)
        self.widget.section_table.selectRow(len(self.widget.sections) - 1)
        self.widget.section_label.setText(section_copy.name)

    def delete_section(self):
        if not (section := self.widget.section):
            return
        self.widget.sections.remove(section)
        refresh_table(self.widget.section_table, self.widget.sections, True)
        self.select_section()

    def select_record(self):
        if not (record := self.widget.record):
            return
        self.widget.record_label.setText(record.name)
        refresh_table(self.widget.buff_table, self.widget.record.buffs)
        refresh_table(self.widget.skill_table, self.widget.record.skills)
        refresh_table(self.widget.dot_table, self.widget.record.dots)

    def add_record(self):
        dialog = RecordEditorDialog(parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.widget.records.append(dialog.record)
            refresh_table(self.widget.record_table, self.widget.records, True)
            self.select_record()

    def edit_record(self):
        if not (record := self.widget.record):
            return
        dialog = RecordEditorDialog(record, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.name = dialog.record.name
            record.count = dialog.record.count
            refresh_table(self.widget.record_table, self.widget.records, True)
            self.widget.record_label.setText(record.name)

    def copy_record(self):
        if not (record := self.widget.record):
            return
        record_copy = deepcopy(record)
        record_copy.name = f"{record_copy.name} - Copy"
        self.widget.records.append(record_copy)
        refresh_table(self.widget.record_table, self.widget.records, True)
        self.widget.record_table.selectRow(len(self.widget.records) - 1)
        self.widget.record_label.setText(record_copy.name)

    def delete_record(self):
        if not (record := self.widget.record):
            return
        self.widget.records.remove(record)
        refresh_table(self.widget.record_table, self.widget.records, True)
        self.select_record()

    def add_buff(self):
        if not (record := self.widget.record):
            return
        dialog = BuffEditorDialog(buffs=self.widget.kungfu.buffs, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (buff := dialog.buff):
            record.buffs.append(buff)
            refresh_table(self.widget.buff_table, record.buffs)

    def edit_buff(self):
        if not (record := self.widget.record):
            return
        buff_index = self.widget.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        dialog = BuffEditorDialog(buffs=self.widget.kungfu.buffs, buff=buff, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.buffs[buff_index] = dialog.buff
            refresh_table(self.widget.buff_table, record.buffs)

    def copy_buff(self):
        if not (record := self.widget.record):
            return
        buff_index = self.widget.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        buff_copy = deepcopy(buff)
        buff_copy.name = f"{buff_copy.name} - Copy"
        record.buffs.append(buff_copy)
        refresh_table(self.widget.buff_table, record.buffs)

    def delete_buff(self):
        if not (record := self.widget.record):
            return
        buff_index = self.widget.buff_table.currentRow()
        if buff_index < 0:
            return
        del record.buffs[buff_index]
        refresh_table(self.widget.buff_table, record.buffs)

    def select_skill(self):
        if not self.widget.record:
            return
        self.show_skill_damage_btn()

    def add_skill(self):
        if not (record := self.widget.record):
            return
        dialog = SkillEditorDialog(skills=self.widget.kungfu.skills, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            record.skills.append(skill)
            refresh_table(self.widget.skill_table, record.skills)
            self.show_skill_damage_btn()

    def edit_skill(self):
        if not (record := self.widget.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        dialog = SkillEditorDialog(skills=self.widget.kungfu.skills, skill=skill, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.skills[skill_index] = dialog.skill
            refresh_table(self.widget.skill_table, record.skills)
            self.show_skill_damage_btn()

    def copy_skill(self):
        if not (record := self.widget.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        skill_copy = deepcopy(skill)
        skill_copy.name = f"{skill_copy.name} - Copy"
        record.skills.append(skill_copy)
        refresh_table(self.widget.skill_table, record.skills)
        self.show_skill_damage_btn()

    def delete_skill(self):
        if not (record := self.widget.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        del record.skills[skill_index]
        refresh_table(self.widget.skill_table, record.skills)
        self.show_skill_damage_btn()

    def select_dot(self):
        if not self.widget.record:
            return
        self.show_dot_damage_btn()

    def add_dot(self):
        if not (record := self.widget.record):
            return
        dialog = DotEditorDialog(dots=self.widget.kungfu.dots, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (dot := dialog.dot) and dot.source:
            record.dots.append(dot)
            refresh_table(self.widget.dot_table, record.dots)
            self.show_dot_damage_btn()

    def edit_dot(self):
        if not (record := self.widget.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dialog = DotEditorDialog(dots=self.widget.kungfu.dots, dot=dot, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and dot.source:
            record.dots[dot_index] = dialog.dot
            refresh_table(self.widget.dot_table, record.dots)
            self.show_dot_damage_btn()

    def copy_dot(self):
        if not (record := self.widget.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dot_copy = deepcopy(dot)
        dot_copy.name = f"{dot_copy.name} - Copy"
        record.dots.append(dot_copy)
        refresh_table(self.widget.dot_table, record.dots)
        self.show_dot_damage_btn()

    def delete_dot(self):
        if not (record := self.widget.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        del record.dots[dot_index]
        refresh_table(self.widget.dot_table, record.dots)
        self.show_dot_damage_btn()

    def init(self, sections: list = None):
        if sections:
            self.widget.sections = sections
        else:
            self.widget.sections = [Section()]
        refresh_table(self.widget.section_table, self.widget.sections, True)
        self.select_section()
        return self.widget.sections
