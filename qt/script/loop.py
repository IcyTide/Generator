from copy import deepcopy

from PySide6.QtWidgets import QDialog

from qt import refresh_table
from qt.classes.buff import BuffType
from qt.classes.kungfu import Kungfu
from qt.classes.section import Section, Sections
from qt.component.loop_widget.attribute_dialog import AttributeDialog
from qt.component.loop_widget.buff_dialog import BuffEditorDialog
from qt.component.loop_widget.damage_dialog import add_buffs_to_attributes
from qt.component.loop_widget.dot_dialog import DotDamageDialog, DotEditorDialog
from qt.component.loop_widget.record_dialog import RecordDamageDialog, RecordEditorDialog
from qt.component.loop_widget.section_dialog import AllDamageDialog, SectionDamageDialog, SectionEditorDialog
from qt.component.loop_widget.skill_dialog import SkillDamageDialog
from qt.component.loop_widget.skill_dialog import SkillEditorDialog
from qt.component.loop_widget.widget import LoopWidget


class LoopScript:
    kungfu: Kungfu
    sections: Sections

    def __init__(self, loop_widget: LoopWidget):
        self.widget = loop_widget

        self.connect()

    @property
    def section(self):
        section_index = self.widget.section_table.currentRow()
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
        record_index = self.widget.record_table.currentRow()
        if record_index < 0:
            return None
        return self.records[record_index]

    def connect(self):
        self.widget.all_damage_btn.clicked.connect(self.show_all_damage)
        self.widget.section_damage_btn.clicked.connect(self.show_section_damage)
        self.widget.record_damage_btn.clicked.connect(self.show_record_damage)
        self.widget.skill_damage_btn.clicked.connect(self.show_skill_damage)
        self.widget.dot_damage_btn.clicked.connect(self.show_dot_damage)
        self.widget.attributes_btn.clicked.connect(self.show_attributes)

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

    def show_attributes(self):
        if not (record := self.record):
            return
        current, snapshot = self.kungfu.create_attribute(), self.kungfu.create_attribute()
        add_buffs_to_attributes(record.buffs, current, snapshot)
        AttributeDialog(current, snapshot, parent=self.widget).exec()

    def show_skill_damage(self):
        if not (record := self.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        attribute = self.kungfu.create_attribute()
        add_buffs_to_attributes(record.buffs, attribute)
        SkillDamageDialog(skill, attribute, parent=self.widget).exec()

    def show_dot_damage(self):
        if not (record := self.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        current, snapshot = self.kungfu.create_attribute(), self.kungfu.create_attribute()
        add_buffs_to_attributes(record.buffs, current, snapshot)
        DotDamageDialog(dot, current, snapshot, parent=self.widget).exec()

    def show_record_damage(self):
        if not (record := self.record):
            return
        if record.is_empty:
            return
        current, snapshot = self.kungfu.create_attribute(), self.kungfu.create_attribute()
        RecordDamageDialog(record, current, snapshot, parent=self.widget).exec()

    def show_section_damage(self):
        if not (section := self.section):
            return
        if section.is_empty:
            return
        current, snapshot = self.kungfu.create_attribute(), self.kungfu.create_attribute()
        SectionDamageDialog(section, current, snapshot, parent=self.widget).exec()

    def show_all_damage(self):
        if self.sections.is_empty:
            return
        current, snapshot = self.kungfu.create_attribute(), self.kungfu.create_attribute()
        AllDamageDialog(self.sections, current, snapshot, parent=self.widget).exec()

    def show_skill_damage_btn(self):
        self.widget.skill_damage_btn.show()
        self.widget.dot_damage_btn.hide()

    def show_dot_damage_btn(self):
        self.widget.skill_damage_btn.hide()
        self.widget.dot_damage_btn.show()

    def show_section_damage_btn(self):
        self.widget.section_damage_btn.show()
        self.widget.record_damage_btn.hide()

    def show_record_damage_btn(self):
        self.widget.record_damage_btn.show()
        self.widget.section_damage_btn.hide()

    def select_section(self):
        if not (section := self.section):
            return
        self.widget.section_label.setText(section.name)
        refresh_table(self.widget.record_table, self.records, True)
        self.select_record()
        self.show_section_damage_btn()

    def add_section(self):
        dialog = SectionEditorDialog(parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections.append(dialog.section)
            refresh_table(self.widget.section_table, self.sections, True)
            self.select_section()
            self.show_section_damage_btn()

    def edit_section(self):
        if not (section := self.section):
            return
        dialog = SectionEditorDialog(section, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.sections[self.widget.section_table.currentRow()] = dialog.section
            refresh_table(self.widget.section_table, self.sections, True)
            self.widget.section_label.setText(dialog.section.name)
            self.show_section_damage_btn()

    def copy_section(self):
        if not (section := self.section):
            return
        section_copy = deepcopy(section)
        section_copy.name = f"{section_copy.name} - Copy"
        self.sections.append(section_copy)
        refresh_table(self.widget.section_table, self.sections, True)
        self.widget.section_table.selectRow(len(self.sections) - 1)
        self.widget.section_label.setText(section_copy.name)
        self.show_section_damage_btn()

    def delete_section(self):
        if not (section := self.section):
            return
        self.sections.remove(section)
        refresh_table(self.widget.section_table, self.sections, True)
        self.select_section()
        self.show_section_damage_btn()

    def select_record(self):
        if not (record := self.record):
            return
        self.widget.record_label.setText(record.name)
        refresh_table(self.widget.buff_table, self.record.buffs)
        refresh_table(self.widget.skill_table, self.record.skills)
        refresh_table(self.widget.dot_table, self.record.dots)
        self.show_record_damage_btn()

    def add_record(self):
        dialog = RecordEditorDialog(parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.records.append(dialog.record)
            refresh_table(self.widget.record_table, self.records, True)
            self.select_record()
            self.show_record_damage_btn()

    def edit_record(self):
        if not (record := self.record):
            return
        dialog = RecordEditorDialog(record, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.records[self.widget.record_table.currentRow()] = dialog.record
            refresh_table(self.widget.record_table, self.records, True)
            self.widget.record_label.setText(record.name)
            self.show_record_damage_btn()

    def copy_record(self):
        if not (record := self.record):
            return
        record_copy = deepcopy(record)
        record_copy.name = f"{record_copy.name} - Copy"
        self.records.append(record_copy)
        refresh_table(self.widget.record_table, self.records, True)
        self.widget.record_table.selectRow(len(self.records) - 1)
        self.widget.record_label.setText(record_copy.name)
        self.show_record_damage_btn()

    def delete_record(self):
        if not (record := self.record):
            return
        self.records.remove(record)
        refresh_table(self.widget.record_table, self.records, True)
        self.select_record()
        self.show_record_damage_btn()

    def add_buff(self):
        if not (record := self.record):
            return
        dialog = BuffEditorDialog(buffs=self.kungfu.buffs, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (buff := dialog.buff):
            record.buffs.append(buff)
            refresh_table(self.widget.buff_table, record.buffs)

    def edit_buff(self):
        if not (record := self.record):
            return
        buff_index = self.widget.buff_table.currentRow()
        if buff_index < 0:
            return
        buff = record.buffs[buff_index]
        dialog = BuffEditorDialog(buffs=self.kungfu.buffs, buff=buff, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.buffs[buff_index] = dialog.buff
            refresh_table(self.widget.buff_table, record.buffs)

    def copy_buff(self):
        if not (record := self.record):
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
        if not (record := self.record):
            return
        buff_index = self.widget.buff_table.currentRow()
        if buff_index < 0:
            return
        del record.buffs[buff_index]
        refresh_table(self.widget.buff_table, record.buffs)

    def select_skill(self):
        if not self.record:
            return
        self.show_skill_damage_btn()

    def add_skill(self):
        if not (record := self.record):
            return
        dialog = SkillEditorDialog(skills=self.kungfu.skills, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (skill := dialog.skill):
            record.skills.append(skill)
            refresh_table(self.widget.skill_table, record.skills)
            self.show_skill_damage_btn()

    def edit_skill(self):
        if not (record := self.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        skill = record.skills[skill_index]
        dialog = SkillEditorDialog(skills=self.kungfu.skills, skill=skill, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            record.skills[skill_index] = dialog.skill
            refresh_table(self.widget.skill_table, record.skills)
            self.show_skill_damage_btn()

    def copy_skill(self):
        if not (record := self.record):
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
        if not (record := self.record):
            return
        skill_index = self.widget.skill_table.currentRow()
        if skill_index < 0:
            return
        del record.skills[skill_index]
        refresh_table(self.widget.skill_table, record.skills)
        self.show_skill_damage_btn()

    def select_dot(self):
        if not self.record:
            return
        self.show_dot_damage_btn()

    def add_dot(self):
        if not (record := self.record):
            return
        dialog = DotEditorDialog(dots=self.kungfu.dots, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and (dot := dialog.dot) and dot.source:
            record.dots.append(dot)
            refresh_table(self.widget.dot_table, record.dots)
            self.show_dot_damage_btn()

    def edit_dot(self):
        if not (record := self.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        dot = record.dots[dot_index]
        dialog = DotEditorDialog(dots=self.kungfu.dots, dot=dot, parent=self.widget)
        if dialog.exec() == QDialog.DialogCode.Accepted and dot.source:
            record.dots[dot_index] = dialog.dot
            refresh_table(self.widget.dot_table, record.dots)
            self.show_dot_damage_btn()

    def copy_dot(self):
        if not (record := self.record):
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
        if not (record := self.record):
            return
        dot_index = self.widget.dot_table.currentRow()
        if dot_index < 0:
            return
        del record.dots[dot_index]
        refresh_table(self.widget.dot_table, record.dots)
        self.show_dot_damage_btn()

    def init(self, kungfu: Kungfu, sections: Sections = None):
        self.kungfu = kungfu
        if sections:
            self.sections = sections
        else:
            self.sections = Sections([Section()])
        refresh_table(self.widget.section_table, self.sections, True)
        self.select_section()
        return self.sections
