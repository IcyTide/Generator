DOTS = {
    10002: {
        235: {
            743: {
                29: {
                    "name": "横扫六合(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        43073: {
                            29: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(45 + solar_attack_power * 0.6571180555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ],
                                "critical_strike": "solar_critical_strike",
                                "critical_power": "solar_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10003: {
        235: {
            743: {
                29: {
                    "name": "横扫六合(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        43073: {
                            29: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(45 + solar_attack_power * 0.6571180555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ],
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                            }
                        }
                    }
                }
            }
        },
        32649: {
            743: {
                29: {
                    "name": "横扫六合(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        28539: {
                            29: {
                                "name": "无执六合环绕",
                                "comment": "",
                                "damages": [
                                    "(45 + solar_attack_power * 0.18402777777777776) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ],
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                            }
                        }
                    }
                }
            }
        },
        24884: {
            743: {
                58: {
                    "name": "横扫六合(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 2,
                    "max_tick": 6,
                    "skills": {
                        43073: {
                            58: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(45 + solar_attack_power * 0.6571180555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ],
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024"
                            }
                        }
                    }
                }
            }
        }
    },
    10014: {},
    10015: {
        588: {
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
        38530: {
            748: {
                1: {
                    "name": "叠刃(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 5,
                    "max_tick": 8,
                    "skills": {
                        600: {
                            1: {
                                "name": "叠刃",
                                "comment": "",
                                "damages": [
                                    "(10 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10021: {
        180: {
            666: {
                29: {
                    "name": "商阳指(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        180: {
                            29: {
                                "name": "商阳指",
                                "comment": "",
                                "damages": [
                                    "(50 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        189: {
            714: {
                24: {
                    "name": "钟林毓秀(DOT)",
                    "comment": "",
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        190: {
            711: {
                19: {
                    "name": "兰摧玉折(DOT)",
                    "comment": "",
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        186: {
            666: {
                29: {
                    "name": "商阳指(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        6134: {
                            29: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(50 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
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
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        6135: {
                            24: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            },
            711: {
                19: {
                    "name": "兰摧玉折(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        6136: {
                            19: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        2645: {
            714: {
                24: {
                    "name": "钟林毓秀(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        39907: {
                            2: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(38 + neutral_attack_power * int(766.27392225541 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            },
            711: {
                19: {
                    "name": "兰摧玉折(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        39906: {
                            2: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(30 + neutral_attack_power * int(882.395546576514 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        30596: {
            666: {
                30: {
                    "name": "商阳指(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        34280: {
                            29: {
                                "name": "",
                                "comment": "1段",
                                "damages": [
                                    "(50 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        },
                        40085: {
                            1: {
                                "name": "",
                                "comment": "2段",
                                "damages": [
                                    "(50 + neutral_attack_power * int(1409.9440169499544 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.050000000000000044 * recipe_1301_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            },
            714: {
                25: {
                    "name": "钟林毓秀(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        34279: {
                            24: {
                                "name": "",
                                "comment": "1段",
                                "damages": [
                                    "(38 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        },
                        40086: {
                            1: {
                                "name": "",
                                "comment": "2段",
                                "damages": [
                                    "(38 + neutral_attack_power * int(1532.54784451082 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.050000000000000044 * recipe_1302_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            },
            711: {
                20: {
                    "name": "兰摧玉折(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        34278: {
                            19: {
                                "name": "",
                                "comment": "1段",
                                "damages": [
                                    "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        },
                        40084: {
                            1: {
                                "name": "",
                                "comment": "2段",
                                "damages": [
                                    "(30 + neutral_attack_power * int(1764.791093153028 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        6682: {
            711: {
                19: {
                    "name": "兰摧玉折(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        13848: {
                            19: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(30 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.050000000000000044 * recipe_1303_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10026: {
        403: {
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
                                    "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1) * (1 + 0.10000000000000009 * recipe_6291_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        18226: {
            12461: {
                30: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 3,
                    "max_tick": 7,
                    "skills": {
                        401: {
                            30: {
                                "name": "破风",
                                "comment": "",
                                "damages": [
                                    "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1) * (1 + 0.10000000000000009 * recipe_6291_1)) * 0.0010044642857142858 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        14821: {
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
                                    "(60 + physical_attack_power * int(802.233892177905 * (1 + 0.19999999999999996 * recipe_3257_1) * (1 + 0.10000000000000009 * recipe_6291_1)) * 0.0008928571428571428 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10028: {},
    10062: {
        403: {
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
            }
        },
        18226: {
            12461: {
                30: {
                    "name": "流血(DOT)",
                    "comment": "",
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
        }
    },
    10080: {},
    10081: {
        2707: {
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
                                "comment": "",
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
        561: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        18716: {
                            28: {
                                "name": "",
                                "comment": "",
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
        2716: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        6207: {
                            28: {
                                "name": "",
                                "comment": "",
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
        23457: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        18716: {
                            28: {
                                "name": "",
                                "comment": "",
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
        6572: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        6207: {
                            28: {
                                "name": "",
                                "comment": "",
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
        21166: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        18716: {
                            28: {
                                "name": "",
                                "comment": "",
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
        24995: {
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
                                "comment": "",
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
        22732: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        18716: {
                            28: {
                                "name": "",
                                "comment": "",
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
        18202: {
            2920: {
                28: {
                    "name": "急曲(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 6,
                    "max_tick": 6,
                    "skills": {
                        6207: {
                            28: {
                                "name": "",
                                "comment": "",
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
        }
    },
    10144: {},
    10175: {
        2211: {
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
                                    "(55 + poison_attack_power * int(573.07536 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        2212: {
            12557: {
                34: {
                    "name": "百足(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 9,
                    "skills": {
                        18700: {
                            34: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(92 + poison_attack_power * int(1222.5839848992002 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        2210: {
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
                                    "(50 + poison_attack_power * 0.6026785714285715) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        6620: {
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
                                    "(80 + poison_attack_power * int(889.6994963999999 * (1 + 0.19999999999999996 * recipe_818_7) * (1 + 0.050000000000000044 * recipe_1528_1) * (1 + 0.030000000000000027 * recipe_796_1) * (1 + 0.040000000000000036 * recipe_797_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike + (200 * recipe_794_1 + 300 * recipe_795_1) / 10000",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        42309: {
            25917: {
                32: {
                    "name": "蛇影(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 2,
                    "max_tick": 6,
                    "skills": {
                        34643: {
                            32: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(55 + poison_attack_power * int(573.07536 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        37351: {
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
                                    "(180 + poison_attack_power * 0.451171875) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        30572: {
            22731: {
                34: {
                    "name": "百足(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 9,
                    "skills": {
                        30579: {
                            34: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(55 + poison_attack_power * int(2322.90957130848 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * 0.92 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10176: {},
    10224: {
        3098: {
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
                                    "(100 + physical_attack_power * int(550.6562231434689 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.10000000000000009 * recipe_6387_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        6775: {
            12663: {
                27: {
                    "name": "穿心(DOT)",
                    "comment": "",
                    "interval": "48 + -16 * recipe_2632_1",
                    "max_stack": 3,
                    "max_tick": 6,
                    "skills": {
                        18815: {
                            15: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(48 + physical_attack_power * int(550.6562231434689 * (1 + 0.10000000000000009 * recipe_6078_1) * (1 + 0.050000000000000044 * recipe_859_1) * (1 + 0.10000000000000009 * recipe_860_1) * (1 + 0.10000000000000009 * recipe_6387_1) * (1 + 0.5 * recipe_2864_1)) * 0.0015625) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10225: {
        3106: {
            3221: {
                1: {
                    "name": "化血(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 8,
                    "skills": {
                        3126: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(90 + poison_attack_power * 0.6223958333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        42475: {
            3221: {
                3: {
                    "name": "化血(DOT)",
                    "comment": "",
                    "interval": "16",
                    "max_stack": 1,
                    "max_tick": 24,
                    "skills": {
                        3126: {
                            3: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(90 + poison_attack_power * 0.622829861111111) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        18675: {
            3221: {
                2: {
                    "name": "化血(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 8,
                    "skills": {
                        3126: {
                            2: {
                                "name": "",
                                "comment": "",
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
                    "comment": "尽刑彻毒+千秋万劫",
                    "interval": "16",
                    "max_stack": 1,
                    "max_tick": 24,
                    "skills": {
                        3126: {
                            4: {
                                "name": "",
                                "comment": "",
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
        }
    },
    10242: {
        3960: {
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
            }
        },
        34372: {
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
        }
    },
    10243: {
        3960: {
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
        }
    },
    10268: {
        5262: {
            6367: {
                20: {
                    "name": "灼烧(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 3,
                    "max_tick": 5,
                    "skills": {
                        6853: {
                            20: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(32 + physical_attack_power * 0.953125) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        6818: {
            6401: {
                20: {
                    "name": "灼烧(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 5,
                    "max_tick": 11,
                    "skills": {
                        6867: {
                            20: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(33 + physical_attack_power * 0.953125) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        14927: {
            32041: {
                1: {
                    "name": "灼烧·御鸿于天(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 5,
                    "max_tick": 16,
                    "skills": {
                        42918: {
                            20: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(33 + physical_attack_power * 0.938232421875) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10389: {
        13054: {
            8249: {
                22: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 13,
                    "skills": {
                        29188: {
                            22: {
                                "name": "",
                                "comment": "",
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
        13132: {
            8249: {
                22: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 13,
                    "skills": {
                        13308: {
                            22: {
                                "name": "",
                                "comment": "闪刀",
                                "damages": [
                                    "(47 + physical_attack_power * 0.46995192307692313 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        },
                        29186: {
                            28: {
                                "name": "",
                                "comment": "斩刀",
                                "damages": [
                                    "(47 + physical_attack_power * 0.2370192307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10390: {
        13054: {
            8249: {
                22: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 13,
                    "skills": {
                        29188: {
                            22: {
                                "name": "",
                                "comment": "",
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
        41740: {
            31385: {
                1: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 3,
                    "max_tick": 13,
                    "skills": {
                        41738: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(60 + physical_attack_power * 0.12463942307692308) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        37558: {
            31385: {
                2: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "16",
                    "max_stack": 3,
                    "max_tick": 26,
                    "skills": {
                        41737: {
                            1: {
                                "name": "",
                                "comment": "",
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
        }
    },
    10447: {
        14065: {
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
                                    "(58 + lunar_attack_power * int(525.6367640870349 * (1 + 0.030000000000000027 * recipe_2058_1) * (1 + 0.040000000000000036 * recipe_2059_1) * (1 + 0.050000000000000044 * recipe_2060_1)) * 0.0013020833333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike + (200 * recipe_2063_1 + 300 * recipe_2064_1 + 400 * recipe_2065_1) / 10000",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        },
        14067: {
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
                                    "(58 + lunar_attack_power * 0.6653645833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        },
        14285: {
            9360: {
                25: {
                    "name": "商(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 9,
                    "skills": {
                        14290: {
                            25: {
                                "name": "商",
                                "comment": "",
                                "damages": [
                                    "(58 + lunar_attack_power * int(788.4551461305523 * (1 + 0.030000000000000027 * recipe_2058_1) * (1 + 0.040000000000000036 * recipe_2059_1) * (1 + 0.050000000000000044 * recipe_2060_1) * 1.12 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
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
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 9,
                    "skills": {
                        14294: {
                            25: {
                                "name": "角",
                                "comment": "",
                                "damages": [
                                    "(58 + lunar_attack_power * int(767.975791685603 * 1.12 ** (tick - 1)) * 0.0008680555555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        },
        34344: {
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
                                    "(26 + rand * 100 + lunar_attack_power * 7.8125) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
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
                                    "(26 + rand * 100 + lunar_attack_power * 2.005208333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
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
                    "max_stack": 5,
                    "max_tick": 8,
                    "skills": {
                        42010: {
                            1: {
                                "name": "青莲剑·徵",
                                "comment": "",
                                "damages": [
                                    "(26 + lunar_attack_power * 0.7682291666666666) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10448: {},
    10464: {
        17057: {
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
                        }
                    }
                }
            }
        },
        17056: {
            11447: {
                10: {
                    "name": "闹须弥(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 8,
                    "skills": {
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
        }
    },
    10533: {
        38669: {
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
                                    "(50 + physical_attack_power * 1.01513671875) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10585: {
        22575: {
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
        }
    },
    10615: {
        25382: {
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
                                    "(26 + neutral_attack_power * 1.2152777777777777) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10626: {},
    10627: {
        27554: {
            20052: {
                10: {
                    "name": "逆乱(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 8,
                    "max_tick": 9,
                    "skills": {
                        27560: {
                            10: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(95 + poison_attack_power * 0.15711805555555555) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        },
        44384: {
            33061: {
                1: {
                    "name": "千枝花·子株(DOT)",
                    "comment": "",
                    "interval": "16",
                    "max_stack": 1,
                    "max_tick": 10,
                    "skills": {
                        44392: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(10 + poison_attack_power * 3.3333333333333335) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ],
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10698: {
        32144: {
            24132: {
                17: {
                    "name": "流血(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 4,
                    "max_tick": 3,
                    "skills": {
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
                        }
                    }
                }
            }
        },
        32586: {
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
        }
    },
    10756: {
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
        }
    },
    10786: {
        38490: {
            33156: {
                1: {
                    "name": "蛰微(DOT)",
                    "comment": "",
                    "interval": "32",
                    "max_stack": 1,
                    "max_tick": 5,
                    "skills": {
                        44511: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(10 + neutral_attack_power * 1.2520833333333332) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        }
    },
    10821: {
        42415: {
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
        }
    },
    0: {
        25768: {
            666: {
                29: {
                    "name": "商阳指(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        13849: {
                            29: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(50 + neutral_attack_power * 0.8333333333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
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
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        13847: {
                            24: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(38 + neutral_attack_power * 0.90625) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
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
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        13848: {
                            19: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(30 + neutral_attack_power * 1.0442708333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ],
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power"
                            }
                        }
                    }
                }
            }
        },
        25769: {
            18512: {
                1: {
                    "name": "气吞长江(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 3,
                    "max_tick": 6,
                    "skills": {
                        25757: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(25 + lunar_attack_power * 2.450520833333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        },
        25781: {
            23187: {
                1: {
                    "name": "神兵·宫(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 3,
                    "max_tick": 10,
                    "skills": {
                        40815: {
                            1: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(58 + lunar_attack_power * 1.375) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                },
                2: {
                    "name": "神兵·剑·羽(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 3,
                    "max_tick": 10,
                    "skills": {
                        40815: {
                            2: {
                                "name": "",
                                "comment": "",
                                "damages": [
                                    "(58 + lunar_attack_power * 1.1458333333333333) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ],
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power"
                            }
                        }
                    }
                }
            }
        },
        25783: {
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
            }
        },
        25784: {
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
                                    "(25 + physical_attack_power * 1.8140625000000001) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 130) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ],
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power"
                            }
                        }
                    }
                }
            }
        },
        43086: {
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
            }
        }
    }
}
