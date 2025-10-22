from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSplitter, QVBoxLayout, QWidget)

from qt import LabelRow, Table


class LoopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        self.all_damage_btn = QPushButton("计算全部伤害")
        top_layout.addWidget(self.all_damage_btn)
        self.section_damage_btn = QPushButton("计算小节伤害")
        top_layout.addWidget(self.section_damage_btn)
        self.record_damage_btn = QPushButton("计算片段伤害")
        top_layout.addWidget(self.record_damage_btn)
        self.record_damage_btn.hide()

        self.skill_damage_btn = QPushButton("计算技能伤害")
        top_layout.addWidget(self.skill_damage_btn)
        self.dot_damage_btn = QPushButton("计算持续伤害")
        top_layout.addWidget(self.dot_damage_btn)
        self.dot_damage_btn.hide()
        self.attributes_btn = QPushButton("当前属性")
        top_layout.addWidget(self.attributes_btn)
        layout.addLayout(top_layout)

        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left Panel - Sections and Records
        left_layout = QVBoxLayout((left_panel := QWidget()))

        # Section Display
        self.section_table = Table(["序号", "名称", "数量", "时长"])
        self.section_label = QLabel("")
        left_layout.addWidget(LabelRow("当前小节:", self.section_label))
        left_layout.addWidget(self.section_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_section_btn = QPushButton("新增小节")
        btn_layout.addWidget(self.add_section_btn)
        self.copy_section_btn = QPushButton("复制小节")
        btn_layout.addWidget(self.copy_section_btn)
        self.del_section_btn = QPushButton("删除小节")
        btn_layout.addWidget(self.del_section_btn)

        # Record Display
        self.record_label = QLabel("")
        left_layout.addWidget(LabelRow("当前片段:", self.record_label))
        self.record_table = Table(["序号", "名称", "数量", "时长"])
        left_layout.addWidget(self.record_table)
        left_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_record_btn = QPushButton("新增片段")
        btn_layout.addWidget(self.add_record_btn)
        self.copy_record_btn = QPushButton("复制片段")
        btn_layout.addWidget(self.copy_record_btn)
        self.del_record_btn = QPushButton("删除片段")
        btn_layout.addWidget(self.del_record_btn)

        # Right Panel - Buff and Skill and Dot
        right_layout = QVBoxLayout((right_panel := QWidget()))

        # Buff Display
        right_layout.addWidget(QLabel("增益清单"))
        self.buff_table = Table(["名称", "ID", "等级", "层数", "类型"])
        right_layout.addWidget(self.buff_table)
        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_buff_btn = QPushButton("新增增益")
        btn_layout.addWidget(self.add_buff_btn)
        self.copy_buff_btn = QPushButton("复制增益")
        btn_layout.addWidget(self.copy_buff_btn)
        self.del_buff_btn = QPushButton("删除增益")
        btn_layout.addWidget(self.del_buff_btn)

        # Skill Display
        right_layout.addWidget(QLabel("技能伤害清单"))
        self.skill_table = Table(["名称", "ID", "等级", "数量"])
        right_layout.addWidget(self.skill_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_skill_btn = QPushButton("新增技能伤害")
        btn_layout.addWidget(self.add_skill_btn)
        self.copy_skill_btn = QPushButton("复制技能伤害")
        btn_layout.addWidget(self.copy_skill_btn)
        self.del_skill_btn = QPushButton("删除技能伤害")
        btn_layout.addWidget(self.del_skill_btn)

        # Dot Display
        right_layout.addWidget(QLabel("持续伤害清单"))
        self.dot_table = Table(["名称", "ID", "等级", "层数/跳数", "数量"])
        right_layout.addWidget(self.dot_table)

        right_layout.addLayout((btn_layout := QHBoxLayout()))
        self.add_dot_btn = QPushButton("新增持续伤害")
        btn_layout.addWidget(self.add_dot_btn)
        self.copy_dot_btn = QPushButton("复制持续伤害")
        btn_layout.addWidget(self.copy_dot_btn)
        self.del_dot_btn = QPushButton("删除持续伤害")
        btn_layout.addWidget(self.del_dot_btn)

        # Main Widget Set
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(right_panel)
        layout.addWidget(main_splitter)
