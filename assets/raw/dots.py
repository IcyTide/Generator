DOTS = {
    10002: {
        743: {
            29: {
                "name": "横扫六合(DOT)",
                "comment": "原始",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    43073: {
                        29: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike",
                            "critical_power": "solar_critical_power"
                        }
                    }
                }
            }
        }
    },
    10003: {
        743: {
            29: {
                "name": "横扫六合(DOT)",
                "comment": "原始",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    43073: {
                        29: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "我闻",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    28539: {
                        29: {
                            "name": "无执六合环绕",
                            "comment": "无诤",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "无执六合环绕",
                            "comment": "无诤(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    43136: {
                        29: {
                            "name": "",
                            "comment": "幻身",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "幻身(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    }
                }
            },
            58: {
                "name": "横扫六合(DOT)",
                "comment": "我闻",
                "interval": "32",
                "max_stack": 2,
                "max_tick": 6,
                "skills": {
                    43073: {
                        29: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "我闻",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    28539: {
                        29: {
                            "name": "无执六合环绕",
                            "comment": "无诤",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "无执六合环绕",
                            "comment": "无诤(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    43136: {
                        29: {
                            "name": "",
                            "comment": "幻身",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "幻身(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    }
                }
            },
            59: {
                "name": "横扫六合·无诤(DOT)",
                "comment": "原始",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    43073: {
                        29: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "我闻",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    28539: {
                        29: {
                            "name": "无执六合环绕",
                            "comment": "无诤",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "无执六合环绕",
                            "comment": "无诤(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    43136: {
                        29: {
                            "name": "",
                            "comment": "幻身",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "幻身(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    }
                }
            },
            60: {
                "name": "横扫六合·无诤(DOT)",
                "comment": "我闻",
                "interval": "32",
                "max_stack": 2,
                "max_tick": 6,
                "skills": {
                    43073: {
                        29: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "我闻",
                            "damages": [
                                "(45 + solar_attack_power * 0.6085069444444444) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    28539: {
                        29: {
                            "name": "无执六合环绕",
                            "comment": "无诤",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "无执六合环绕",
                            "comment": "无诤(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 0.17013888888888887) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    43136: {
                        29: {
                            "name": "",
                            "comment": "幻身",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        },
                        58: {
                            "name": "",
                            "comment": "幻身(我闻)",
                            "damages": [
                                "(45 + solar_attack_power * 1.0043402777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                            "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    }
                }
            }
        }
    },
    10014: {},
    10015: {
        748: {
            1: {
                "name": "叠刃(DOT)",
                "comment": "原始",
                "interval": "48",
                "max_stack": 5,
                "max_tick": 8,
                "skills": {
                    600: {
                        1: {
                            "name": "叠刃",
                            "comment": "原始",
                            "damages": [
                                "(10 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "叠刃",
                            "comment": "裂云",
                            "damages": [
                                "(10 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            2: {
                "name": "叠刃(DOT)",
                "comment": "裂云",
                "interval": "48",
                "max_stack": 7,
                "max_tick": 8,
                "skills": {
                    600: {
                        1: {
                            "name": "叠刃",
                            "comment": "原始",
                            "damages": [
                                "(10 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "叠刃",
                            "comment": "裂云",
                            "damages": [
                                "(10 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        889: {
            1: {
                "name": "人剑合一(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 4,
                "skills": {
                    37453: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(16 + physical_attack_power * 0.703125) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10021: {
        666: {
            29: {
                "name": "商阳指(DOT)",
                "comment": "原始",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    180: {
                        29: {
                            "name": "商阳指",
                            "comment": "",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6134: {
                        29: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2440_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2440_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    34280: {
                        29: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40085: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(50 + neutral_attack_power * int(1281.7672881363221 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13849: {
                        29: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            },
            30: {
                "name": "商阳指(DOT)",
                "comment": "飞白",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    180: {
                        29: {
                            "name": "商阳指",
                            "comment": "",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6134: {
                        29: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2440_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2440_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    34280: {
                        29: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40085: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(50 + neutral_attack_power * int(1281.7672881363221 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13849: {
                        29: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(50 + neutral_attack_power * int(582.6214946074191 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            }
        },
        714: {
            24: {
                "name": "钟林毓秀(DOT)",
                "comment": "原始",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    285: {
                        24: {
                            "name": "钟林毓秀",
                            "comment": "",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6135: {
                        24: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2442_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2442_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    39907: {
                        1: {
                            "name": "",
                            "comment": "乱洒青荷",
                            "damages": [
                                "(38 + neutral_attack_power * int(835.9351879149925 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "渲青",
                            "damages": [
                                "(38 + neutral_attack_power * int(766.27392225541 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    34279: {
                        24: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40086: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(38 + neutral_attack_power * int(1532.54784451082 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13847: {
                        24: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            },
            25: {
                "name": "钟林毓秀(DOT)",
                "comment": "飞白",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    285: {
                        24: {
                            "name": "钟林毓秀",
                            "comment": "",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6135: {
                        24: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2442_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2442_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    39907: {
                        1: {
                            "name": "",
                            "comment": "乱洒青荷",
                            "damages": [
                                "(38 + neutral_attack_power * int(835.9351879149925 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "渲青",
                            "damages": [
                                "(38 + neutral_attack_power * int(766.27392225541 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    34279: {
                        24: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40086: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(38 + neutral_attack_power * int(1532.54784451082 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13847: {
                        24: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            }
        },
        711: {
            19: {
                "name": "兰摧玉折(DOT)",
                "comment": "原始",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    18730: {
                        19: {
                            "name": "兰摧玉折",
                            "comment": "",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6136: {
                        19: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2441_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2441_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    39906: {
                        1: {
                            "name": "",
                            "comment": "乱洒青荷",
                            "damages": [
                                "(30 + neutral_attack_power * int(962.613323538015 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "渲青",
                            "damages": [
                                "(30 + neutral_attack_power * int(882.395546576514 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    34278: {
                        19: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40084: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(30 + neutral_attack_power * int(1764.791093153028 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13848: {
                        19: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            },
            20: {
                "name": "兰摧玉折(DOT)",
                "comment": "飞白",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    18730: {
                        19: {
                            "name": "兰摧玉折",
                            "comment": "",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    6136: {
                        19: {
                            "name": "",
                            "comment": "芙蓉并蒂",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike + 1500 * recipe_2441_1 / 10000",
                            "critical_power": "min(3,neutral_critical_power_percent + (154 * recipe_2441_1 + neutral_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    },
                    39906: {
                        1: {
                            "name": "",
                            "comment": "乱洒青荷",
                            "damages": [
                                "(30 + neutral_attack_power * int(962.613323538015 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "渲青",
                            "damages": [
                                "(30 + neutral_attack_power * int(882.395546576514 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    34278: {
                        19: {
                            "name": "",
                            "comment": "飞白1段",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    40084: {
                        1: {
                            "name": "",
                            "comment": "飞白2段",
                            "damages": [
                                "(30 + neutral_attack_power * int(1764.791093153028 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    },
                    13848: {
                        19: {
                            "name": "",
                            "comment": "风烟翠/随墨/流离",
                            "damages": [
                                "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            }
        }
    },
    10026: {
        3442: {
            30: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "32 + -8 * recipe_2498_1",
                "max_stack": 2,
                "max_tick": 7,
                "skills": {
                    18591: {
                        30: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        12461: {
            30: {
                "name": "流血(DOT)",
                "comment": "击水",
                "interval": "32",
                "max_stack": 3,
                "max_tick": 7,
                "skills": {
                    401: {
                        30: {
                            "name": "破风",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        19317: {
            30: {
                "name": "流血(DOT)",
                "comment": "击水+牙璋",
                "interval": "28",
                "max_stack": 3,
                "max_tick": 7,
                "skills": {
                    26773: {
                        30: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1)) * 0.0008928571428571428 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10028: {},
    10062: {
        3442: {
            30: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 2,
                "max_tick": 7,
                "skills": {
                    18591: {
                        30: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        12461: {
            30: {
                "name": "流血(DOT)",
                "comment": "击水",
                "interval": "32",
                "max_stack": 3,
                "max_tick": 7,
                "skills": {
                    401: {
                        30: {
                            "name": "破风",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10080: {},
    10081: {
        18512: {
            1: {
                "name": "气吞长江(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 10,
                "skills": {
                    25757: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(25 + lunar_attack_power * 1.4674479166666665) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        2920: {
            28: {
                "name": "急曲(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 6,
                "max_tick": 6,
                "skills": {
                    3009: {
                        28: {
                            "name": "玳弦急曲",
                            "comment": "玳弦急曲/盈袖",
                            "damages": [
                                "(100 + lunar_attack_power * 0.17838541666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    },
                    6207: {
                        28: {
                            "name": "",
                            "comment": "剑破虚空/玉素/耐夜",
                            "damages": [
                                "(100 + lunar_attack_power * 0.17838541666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    },
                    18716: {
                        28: {
                            "name": "",
                            "comment": "剑气长江/琼霄/霜天剑泠/钗燕/镜花",
                            "damages": [
                                "(100 + lunar_attack_power * 0.17838541666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        }
    },
    10144: {},
    10175: {
        2296: {
            32: {
                "name": "蛇影(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    6237: {
                        32: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(55 + poison_attack_power * int(477.56280000000004 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1) * (1 + 0.25 * recipe_1269_1) * (1 + 0.6000000000000001 * recipe_5891_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        2509: {
            34: {
                "name": "百足(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    6238: {
                        34: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(92 + poison_attack_power * int(679.2133249440002 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * (1 + 0.25 * recipe_1270_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        2295: {
            26: {
                "name": "蟾啸(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 7,
                "skills": {
                    6236: {
                        26: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(50 + poison_attack_power * int(600.3148074000001 * (1 + 0.25 * recipe_1271_1) * (1 + 0.6000000000000001 * recipe_5901_1)) * 0.0008370535714285715) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        6218: {
            31: {
                "name": "蝎心(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    13476: {
                        31: {
                            "name": "蝎心",
                            "comment": "",
                            "damages": [
                                "(80 + poison_attack_power * int(741.416247 * (1 + 0.19999999999999996 * recipe_818_7) * (1 + 0.050000000000000044 * recipe_1528_1) * (1 + 0.030000000000000027 * recipe_796_1) * (1 + 0.040000000000000036 * recipe_797_1) * (1 + 0.25 * recipe_1272_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike + (200 * recipe_794_1 + 300 * recipe_795_1) / 10000",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        22730: {
            34: {
                "name": "百足(DOT)",
                "comment": "不僵",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    30578: {
                        34: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(92 + poison_attack_power * int(1358.4266498880004 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * 0.94 ** (tick - 1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        22731: {
            34: {
                "name": "百足(DOT)",
                "comment": "不僵+固灵",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    30579: {
                        34: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(55 + poison_attack_power * int(2037.6399748320005 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * 0.94 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        25917: {
            32: {
                "name": "蛇影(DOT)",
                "comment": "腾影",
                "interval": "32",
                "max_stack": 2,
                "max_tick": 6,
                "skills": {
                    34643: {
                        32: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(55 + poison_attack_power * int(477.56280000000004 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1) * (1 + 0.25 * recipe_3263_1) * (1 + 0.6000000000000001 * recipe_5891_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        28210: {
            1: {
                "name": "释灵(DOT)",
                "comment": "",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    37352: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(180 + poison_attack_power * int(693.3333333333334 * (1 + 0.25 * recipe_5538_1)) * 0.0006510416666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        },
        12557: {
            34: {
                "name": "百足(DOT)",
                "comment": "固灵",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    18700: {
                        34: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(92 + poison_attack_power * int(1018.8199874160002 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * (1 + 0.25 * recipe_4550_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        }
    },
    10176: {},
    10224: {
        2237: {
            29: {
                "name": "穿心(DOT)",
                "comment": "",
                "interval": "48 + -16 * recipe_2632_1",
                "max_stack": 2,
                "max_tick": 6,
                "skills": {
                    3125: {
                        15: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(100 + physical_attack_power * int(550.6562231434689 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29148: {
                        15: {
                            "name": "",
                            "comment": "鹰扬虎视",
                            "damages": [
                                "(100 + physical_attack_power * int(633.2546566149892 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        12663: {
            27: {
                "name": "穿心(DOT)",
                "comment": "摧心",
                "interval": "48 + -16 * recipe_2632_1",
                "max_stack": 3,
                "max_tick": 6,
                "skills": {
                    18815: {
                        15: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(48 + physical_attack_power * int(550.6562231434689 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29154: {
                        15: {
                            "name": "",
                            "comment": "鹰扬虎视",
                            "damages": [
                                "(48 + physical_attack_power * int(633.2546566149892 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10225: {
        3221: {
            1: {
                "name": "化血(DOT)",
                "comment": "原始",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    3126: {
                        1: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(90 + poison_attack_power * 0.6223958333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "千秋万劫",
                            "damages": [
                                "(90 + poison_attack_power * 1.24609375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        3: {
                            "name": "",
                            "comment": "尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 1.8684895833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        4: {
                            "name": "",
                            "comment": "千秋万劫+尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 3.73828125) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            2: {
                "name": "化血(DOT)",
                "comment": "千秋万劫",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    3126: {
                        1: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(90 + poison_attack_power * 0.6223958333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "千秋万劫",
                            "damages": [
                                "(90 + poison_attack_power * 1.24609375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        3: {
                            "name": "",
                            "comment": "尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 1.8684895833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        4: {
                            "name": "",
                            "comment": "千秋万劫+尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 3.73828125) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            3: {
                "name": "化血(DOT)",
                "comment": "尽刑彻毒",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 24,
                "skills": {
                    3126: {
                        1: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(90 + poison_attack_power * 0.20746527777777776) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "千秋万劫",
                            "damages": [
                                "(90 + poison_attack_power * 0.4153645833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        3: {
                            "name": "",
                            "comment": "尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 0.622829861111111) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        4: {
                            "name": "",
                            "comment": "千秋万劫+尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 1.24609375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            4: {
                "name": "化血(DOT)",
                "comment": "千秋万劫+尽刑彻毒",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 24,
                "skills": {
                    3126: {
                        1: {
                            "name": "",
                            "comment": "原始",
                            "damages": [
                                "(90 + poison_attack_power * 0.20746527777777776) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "千秋万劫",
                            "damages": [
                                "(90 + poison_attack_power * 0.4153645833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        3: {
                            "name": "",
                            "comment": "尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 0.622829861111111) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        },
                        4: {
                            "name": "",
                            "comment": "千秋万劫+尽刑彻毒",
                            "damages": [
                                "(90 + poison_attack_power * 1.24609375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10242: {
        4202: {
            18: {
                "name": "银月斩(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    13359: {
                        18: {
                            "name": "银月斩",
                            "comment": "",
                            "damages": [
                                "(55 + lunar_attack_power * 0.2986111111111111) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + (500 * recipe_1148_1 + 300 * recipe_992_1 + 400 * recipe_993_1 + 500 * recipe_994_1) / 10000",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        25725: {
            1: {
                "name": "靡业报劫·日(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 10,
                "skills": {
                    34373: {
                        4: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(30 + (solar_attack_power + base_solar_attack_power * 184 * recipe_3222_1 / 1024) * 2.246223958333333) * (1 + magical_damage_addition + (31 * recipe_1621_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 - 31 * recipe_1621_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 + 51 * recipe_1623_1 - 31 * recipe_1621_1 + 41 * recipe_1622_1) / 1024) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                            ],
                            "critical_strike": "solar_critical_strike + 10000 * recipe_4545_1 / 10000",
                            "critical_power": "solar_critical_power"
                        }
                    }
                }
            }
        },
        25726: {
            1: {
                "name": "靡业报劫·月(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 10,
                "skills": {
                    34374: {
                        4: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(30 + (lunar_attack_power + base_lunar_attack_power * 184 * recipe_3225_1 / 1024) * 2.246223958333333) * (1 + magical_damage_addition + (31 * recipe_1621_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 - 31 * recipe_1621_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 + 51 * recipe_1623_1 - 31 * recipe_1621_1 + 41 * recipe_1622_1) / 1024) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + 10000 * recipe_4545_1 / 10000",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        }
    },
    10243: {
        4202: {
            18: {
                "name": "银月斩(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    13359: {
                        18: {
                            "name": "银月斩",
                            "comment": "",
                            "damages": [
                                "(55 + lunar_attack_power * 0.2986111111111111) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + (300 * recipe_992_1 + 400 * recipe_993_1 + 500 * recipe_994_1) / 10000",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        }
    },
    10268: {
        6367: {
            20: {
                "name": "灼烧(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 5,
                "max_tick": 5,
                "skills": {
                    6853: {
                        20: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(32 + physical_attack_power * 0.4765625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        6401: {
            20: {
                "name": "灼烧(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 10,
                "max_tick": 10,
                "skills": {
                    6867: {
                        20: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(33 + physical_attack_power * 0.4765625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        32041: {
            1: {
                "name": "灼烧·御鸿于天(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 10,
                "max_tick": 15,
                "skills": {
                    42918: {
                        20: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(33 + physical_attack_power * 0.47604166666666664) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10389: {
        8249: {
            22: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 13,
                "skills": {
                    29188: {
                        28: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(47 + physical_attack_power * 0.12463942307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    13308: {
                        22: {
                            "name": "",
                            "comment": "闪刀割裂",
                            "damages": [
                                "(47 + physical_attack_power * 0.46995192307692313 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    20989: {
                        22: {
                            "name": "",
                            "comment": "闪刀割裂+炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.4740384615384616 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29185: {
                        28: {
                            "name": "",
                            "comment": "斩刀割裂+炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.5210336538461539) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29186: {
                        28: {
                            "name": "",
                            "comment": "斩刀割裂",
                            "damages": [
                                "(47 + physical_attack_power * 0.2370192307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29187: {
                        28: {
                            "name": "",
                            "comment": "斩刀炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.24927884615384616) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            50: {
                "name": "流血(DOT)",
                "comment": "炼狱",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 26,
                "skills": {
                    29188: {
                        28: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(47 + physical_attack_power * 0.06231971153846154) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    13308: {
                        22: {
                            "name": "",
                            "comment": "闪刀割裂",
                            "damages": [
                                "(47 + physical_attack_power * 0.23497596153846156 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    20989: {
                        22: {
                            "name": "",
                            "comment": "闪刀割裂+炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.2370192307692308 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29185: {
                        28: {
                            "name": "",
                            "comment": "斩刀割裂+炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.2605168269230769) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29186: {
                        28: {
                            "name": "",
                            "comment": "斩刀割裂",
                            "damages": [
                                "(47 + physical_attack_power * 0.1185096153846154) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    29187: {
                        28: {
                            "name": "",
                            "comment": "斩刀炼狱",
                            "damages": [
                                "(47 + physical_attack_power * 0.12463942307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10390: {
        8249: {
            56: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 26,
                "skills": {
                    29188: {
                        28: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(60 + physical_attack_power * 0.06231971153846154) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        31385: {
            1: {
                "name": "流血(DOT)",
                "comment": "崩血",
                "interval": "32",
                "max_stack": 3,
                "max_tick": 13,
                "skills": {
                    41738: {
                        1: {
                            "name": "",
                            "comment": "崩血+登锋",
                            "damages": [
                                "(60 + physical_attack_power * 0.12463942307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    41737: {
                        1: {
                            "name": "",
                            "comment": "登锋",
                            "damages": [
                                "(60 + physical_attack_power * int(244.49039999999997 * (1 + 0.8 * recipe_5562_1)) * 0.0010216346153846154) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            },
            2: {
                "name": "流血(DOT)",
                "comment": "崩血+登锋",
                "interval": "16",
                "max_stack": 3,
                "max_tick": 26,
                "skills": {
                    41738: {
                        1: {
                            "name": "",
                            "comment": "崩血+登锋",
                            "damages": [
                                "(60 + physical_attack_power * 0.06231971153846154) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    41737: {
                        1: {
                            "name": "",
                            "comment": "登锋",
                            "damages": [
                                "(60 + physical_attack_power * int(244.49039999999997 * (1 + 0.8 * recipe_5562_1)) * 0.0005108173076923077) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10447: {
        23187: {
            2: {
                "name": "神兵·剑·羽(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 10,
                "skills": {
                    40815: {
                        1: {
                            "name": "",
                            "comment": "羽",
                            "damages": [
                                "(58 + lunar_attack_power * 1.375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "剑·羽",
                            "damages": [
                                "(58 + lunar_attack_power * 1.1458333333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            },
            3: {
                "name": "神兵·羽(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 10,
                "skills": {
                    40815: {
                        1: {
                            "name": "",
                            "comment": "羽",
                            "damages": [
                                "(58 + lunar_attack_power * 1.375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        },
                        2: {
                            "name": "",
                            "comment": "剑·羽",
                            "damages": [
                                "(58 + lunar_attack_power * 1.1458333333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        9357: {
            25: {
                "name": "商(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    14287: {
                        25: {
                            "name": "商",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * int(477.8516037154862 * (1 + 0.030000000000000027 * recipe_2058_1) * (1 + 0.040000000000000036 * recipe_2059_1) * (1 + 0.050000000000000044 * recipe_2060_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + (200 * recipe_2063_1 + 300 * recipe_2064_1 + 400 * recipe_2065_1) / 10000",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        9361: {
            25: {
                "name": "角(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    14291: {
                        25: {
                            "name": "角",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * 0.60546875) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        9360: {
            25: {
                "name": "商(DOT)",
                "comment": "殊曲",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    14290: {
                        25: {
                            "name": "商",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * int(716.7774055732293 * (1 + 0.030000000000000027 * recipe_2058_1) * (1 + 0.040000000000000036 * recipe_2059_1) * (1 + 0.050000000000000044 * recipe_2060_1) * 1.12 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + (200 * recipe_2063_1 + 300 * recipe_2064_1 + 400 * recipe_2065_1) / 10000",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        9364: {
            25: {
                "name": "角(DOT)",
                "comment": "殊曲",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 9,
                "skills": {
                    14294: {
                        25: {
                            "name": "角",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * int(698.1598106232753 * 1.12 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        31544: {
            1: {
                "name": "青莲剑·徵(DOT)",
                "comment": "",
                "interval": "4",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    42010: {
                        1: {
                            "name": "青莲剑·徵",
                            "comment": "",
                            "damages": [
                                "(26 + lunar_attack_power * 1.4322916666666665) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        31545: {
            1: {
                "name": "青莲剑·角(DOT)",
                "comment": "",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 4,
                "skills": {
                    42009: {
                        1: {
                            "name": "青莲剑·角",
                            "comment": "",
                            "damages": [
                                "(26 + rand * 100 + lunar_attack_power * 2.5260416666666665) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        31546: {
            1: {
                "name": "青莲剑·商(DOT)",
                "comment": "",
                "interval": "24",
                "max_stack": 1,
                "max_tick": 1,
                "skills": {
                    42008: {
                        1: {
                            "name": "青莲剑·商",
                            "comment": "",
                            "damages": [
                                "(26 + rand * 100 + lunar_attack_power * 9.895833333333332) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        }
    },
    10448: {},
    10464: {
        11447: {
            10: {
                "name": "闹须弥(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    17058: {
                        10: {
                            "name": "闹须弥",
                            "comment": "",
                            "damages": [
                                "(52 + physical_attack_power * int(560 * (1 + 0.7 * recipe_4319_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    17060: {
                        10: {
                            "name": "闹须弥",
                            "comment": "",
                            "damages": [
                                "(52 + physical_attack_power * 1.4875) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10533: {
        19557: {
            1: {
                "name": "御波驾澜(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 6,
                "skills": {
                    26935: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(25 + physical_attack_power * 1.0625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        29350: {
            1: {
                "name": "青冥(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    38675: {
                        4: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(50 + physical_attack_power * 2.0302734375) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10585: {
        19626: {
            1: {
                "name": "乍起狂澜(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 6,
                "skills": {
                    26980: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(25 + physical_attack_power * 0.90625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        15568: {
            1: {
                "name": "寂洪荒(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 5,
                "skills": {
                    22330: {
                        32: {
                            "name": "寂洪荒",
                            "comment": "",
                            "damages": [
                                "(25 + physical_attack_power * 0.74375) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike + (500 * recipe_5093_1 + 300 * recipe_6059_1) / 10000",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10615: {
        31796: {
            1: {
                "name": "知微(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 2,
                "max_tick": 15,
                "skills": {
                    42432: {
                        1: {
                            "name": "知微",
                            "comment": "",
                            "damages": [
                                "(26 + neutral_attack_power * 1.0980902777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            }
        }
    },
    10626: {},
    10627: {
        20052: {
            10: {
                "name": "逆乱(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 8,
                "max_tick": 8,
                "skills": {
                    27560: {
                        10: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(95 + poison_attack_power * 0.1546630859375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        }
    },
    10756: {
        26856: {
            1: {
                "name": "贯穿(DOT)",
                "comment": "",
                "interval": "8",
                "max_stack": 6,
                "max_tick": 4,
                "skills": {
                    35771: {
                        6: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(32 + physical_attack_power * 0.23750000000000002) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10698: {
        24132: {
            17: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 4,
                "max_tick": 3,
                "skills": {
                    32369: {
                        17: {
                            "name": "",
                            "comment": "4层流血",
                            "damages": [
                                "(108 + physical_attack_power * 0.34375 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike + (300 * recipe_3055_1 + 400 * recipe_3056_1) / 10000",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    32370: {
                        17: {
                            "name": "",
                            "comment": "3层流血",
                            "damages": [
                                "(108 + physical_attack_power * 0.34375 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike + (300 * recipe_3055_1 + 400 * recipe_3056_1) / 10000",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    32371: {
                        17: {
                            "name": "",
                            "comment": "2层流血",
                            "damages": [
                                "(108 + physical_attack_power * 0.34375 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike + (300 * recipe_3055_1 + 400 * recipe_3056_1) / 10000",
                            "critical_power": "physical_critical_power"
                        }
                    },
                    32372: {
                        17: {
                            "name": "",
                            "comment": "1层流血",
                            "damages": [
                                "(108 + physical_attack_power * 0.34375 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike + (300 * recipe_3055_1 + 400 * recipe_3056_1) / 10000",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        },
        24650: {
            1: {
                "name": "截辕(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    33133: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(102 + physical_attack_power * 0.34375) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    10786: {},
    10821: {
        32145: {
            1: {
                "name": "刻木(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 3,
                "max_tick": 5,
                "skills": {
                    43082: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * 1.5625) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        31705: {
            1: {
                "name": "拘意(DOT)",
                "comment": "",
                "interval": "48",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    42275: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * 0.390625) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike",
                            "critical_power": "lunar_critical_power"
                        }
                    }
                }
            }
        },
        31945: {
            1: {
                "name": "千里急(DOT)",
                "comment": "",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 5,
                "skills": {
                    42702: {
                        1: {
                            "name": "千里急",
                            "comment": "",
                            "damages": [
                                "(58 + lunar_attack_power * int(1200 * (1 + 0.25 * recipe_6052_1) * (1 + 1.2000000000000002 * recipe_6002_1) * (1 + -0.6 * recipe_6182_1) * (1 + -0.8 * recipe_6182_2) * (1 + 0.030000000000000027 * recipe_6145_1) * (1 + 0.040000000000000036 * recipe_6146_1)) * 0.0010416666666666667) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                            ],
                            "critical_strike": "lunar_critical_strike + (200 * recipe_6143_1 + 300 * recipe_6144_1 + 1500 * recipe_6087_1) / 10000",
                            "critical_power": "min(3,lunar_critical_power_percent + (157 * recipe_6087_1 + lunar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                        }
                    }
                }
            }
        }
    },
    100398: {},
    100994: {
        70364: {
            1: {
                "name": "流血(DOT)",
                "comment": "",
                "interval": "32",
                "max_stack": 1,
                "max_tick": 8,
                "skills": {
                    101068: {
                        1: {
                            "name": "闹须弥·悟",
                            "comment": "",
                            "damages": [
                                "(25 + physical_attack_power * 0.7875000000000001) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                            ],
                            "critical_strike": "physical_critical_strike",
                            "critical_power": "physical_critical_power"
                        }
                    }
                }
            }
        }
    },
    101355: {
        71171: {
            1: {
                "name": "中毒(DOT)",
                "comment": "",
                "interval": "16",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    101417: {
                        1: {
                            "name": "无方中和",
                            "comment": "",
                            "damages": [
                                "(1 + poison_attack_power * 0.5807291666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    },
                    102374: {
                        1: {
                            "name": "回风微澜·悟",
                            "comment": "",
                            "damages": [
                                "(1 + poison_attack_power * 0.5807291666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                            ],
                            "critical_strike": "poison_critical_strike",
                            "critical_power": "poison_critical_power"
                        }
                    }
                }
            }
        }
    },
    101450: {
        71316: {
            1: {
                "name": "鸿蒙天禁·悟(DOT)",
                "comment": "",
                "interval": "8",
                "max_stack": 1,
                "max_tick": 6,
                "skills": {
                    102194: {
                        1: {
                            "name": "",
                            "comment": "",
                            "damages": [
                                "(1 + neutral_attack_power * 1.25) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                            ],
                            "critical_strike": "neutral_critical_strike",
                            "critical_power": "neutral_critical_power"
                        }
                    }
                }
            }
        }
    },
    102278: {},
    102393: {},
    0: {}
}
