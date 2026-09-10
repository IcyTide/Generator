DOTS = {
    0: {},
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
                                "critical_strike": "solar_critical_strike",
                                "critical_power": "solar_critical_power",
                                "damages": [
                                    "(1 + solar_attack_power * 0.08125322501241575) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ]
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
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024",
                                "damages": [
                                    "(1 + solar_attack_power * 0.08125322501241575) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ]
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
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024",
                                "damages": [
                                    "(1 + solar_attack_power * 0.022755196436766364) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ]
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
                                "critical_strike": "solar_critical_strike + 1000 * recipe_5157_1 / 10000",
                                "critical_power": "min(3,solar_critical_power_percent + (205 * recipe_5157_1 + solar_critical_power_rate) / 1024) + unlimit_critical_power_rate / 1024",
                                "damages": [
                                    "(1 + solar_attack_power * 0.08125322501241575) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.07818986283510299) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * int(126 * (1 + 0.44999999999999996 * recipe_4583_1)) * 0.0001737552507446733) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.1499999999999999 * recipe_1301_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.1499999999999999 * recipe_1302_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.1499999999999999 * recipe_1301_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.1499999999999999 * recipe_1302_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        },
        2645: {
            666: {
                29: {
                    "name": "商阳指(DOT)",
                    "comment": "",
                    "interval": "48",
                    "max_stack": 1,
                    "max_tick": 6,
                    "skills": {
                        46099: {
                            1: {
                                "name": "",
                                "comment": "",
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(769.0603728817932 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.1499999999999999 * recipe_1301_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                        39907: {
                            1: {
                                "name": "",
                                "comment": "",
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(835.9351879149925 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.1499999999999999 * recipe_1302_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                            1: {
                                "name": "",
                                "comment": "",
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(962.613323538015 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(640.8836440681611 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.1499999999999999 * recipe_1301_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
                            }
                        },
                        40085: {
                            3: {
                                "name": "",
                                "comment": "2段",
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(1550.93841864495 * (1 + 1.2000000000000002 * recipe_2941_1) * (1 + 0.1499999999999999 * recipe_1301_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(696.6126565958272 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.1499999999999999 * recipe_1302_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
                            }
                        },
                        40086: {
                            3: {
                                "name": "",
                                "comment": "2段",
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6312_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(1685.802628961902 * (1 + 0.1499999999999999 * recipe_817_1) * (1 + 1.2000000000000002 * recipe_2942_1) * (1 + 0.1499999999999999 * recipe_1302_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
                            }
                        },
                        40084: {
                            3: {
                                "name": "",
                                "comment": "2段",
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(1941.270202468331 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike + 1000 * recipe_6311_1 / 10000",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * int(802.1777696150126 * (1 + 1.2000000000000002 * recipe_2940_1) * (1 + 0.1499999999999999 * recipe_1303_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
    10028: {},
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6530_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6508_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6530_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6508_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6530_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6530_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * int(137.18133000000003 * (1 + recipe_6508_1) * (1.0 + 0.05 * buff_29462_1)) * 0.0001610037483733469) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
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
                                "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(573.07536 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(1222.5839848992002 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * 0.07452173496137772) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike + (200 * recipe_794_1 + 300 * recipe_795_1) / 10000",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(889.6994963999999 * (1 + 0.19999999999999996 * recipe_818_7) * (1 + 0.050000000000000044 * recipe_1528_1) * (1 + 0.030000000000000027 * recipe_796_1) * (1 + 0.040000000000000036 * recipe_797_1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike + (200 * recipe_762_1 + 300 * recipe_763_1 + 400 * recipe_764_1) / 10000",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(573.07536 * (1 + 0.10000000000000009 * recipe_4678_1) * (1 + 0.040000000000000036 * recipe_767_1) * (1 + 0.050000000000000044 * recipe_768_1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * 0.06134242813024517) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(2322.90957130848 * (1 + 0.10000000000000009 * recipe_773_1) * (1 + 0.050000000000000044 * recipe_774_1) * (1 + 0.10000000000000009 * recipe_775_1) * 0.92 ** (tick - 1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
    10176: {},
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
                                "critical_strike": "lunar_critical_strike + (500 * recipe_1148_1 + 300 * recipe_992_1 + 400 * recipe_993_1 + 500 * recipe_994_1) / 10000",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * 0.0369235262936209) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "solar_critical_strike + 10000 * recipe_4545_1 / 10000",
                                "critical_power": "solar_critical_power",
                                "damages": [
                                    "(1 + (solar_attack_power + base_solar_attack_power * 184 * recipe_3222_1 / 1024) * 0.3471321316803546) * (1 + magical_damage_addition + (614 * recipe_5908_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 + 51 * recipe_1623_1) / 1024) * (1 + skill_damage_final_addition) * (1 + solar_overcome) * (1 - solar_shield * (1 - all_shield_ignore / 1024) / (solar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + solar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike + 10000 * recipe_4545_1 / 10000",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + (lunar_attack_power + base_lunar_attack_power * 184 * recipe_3225_1 / 1024) * 0.3471321316803546) * (1 + magical_damage_addition + (614 * recipe_5908_1 + 31 * recipe_1621_1 + 41 * recipe_1622_1 + 51 * recipe_1623_1) / 1024) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "lunar_critical_strike + (300 * recipe_992_1 + 400 * recipe_993_1 + 500 * recipe_994_1) / 10000",
                                "critical_power": "lunar_critical_power",
                                "damages": [
                                    "(1 + lunar_attack_power * 0.0369235262936209) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + lunar_overcome) * (1 - lunar_shield * (1 - all_shield_ignore / 1024) / (lunar_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + lunar_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.10599070295425071) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.10599070295425071) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.10433459822059056) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.013860322694017404) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.05226023310859021 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
                            }
                        },
                        29186: {
                            28: {
                                "name": "",
                                "comment": "斩刀",
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.02635733495911506) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.013860322694017404) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.013860322694017404) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * int(244.49039999999997 * (1 + 0.8 * recipe_5562_1)) * 5.680460120498936e-05) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * int(560 * (1 + 0.7 * recipe_4319_1)) * 0.0001737552507446733) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.16541499870892898) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.12976259319675634) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "neutral_critical_strike",
                                "critical_power": "neutral_critical_power",
                                "damages": [
                                    "(1 + neutral_attack_power * 0.15027016514845712) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + neutral_overcome) * (1 - neutral_shield * (1 - all_shield_ignore / 1024) / (neutral_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + neutral_damage_scale)"
                                ]
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
                            20: {
                                "name": "",
                                "comment": "",
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * int(181.12248000000005 * (1 + 0.5 * recipe_6519_1)) * 0.00010733583224889795) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                                "critical_strike": "poison_critical_strike",
                                "critical_power": "poison_critical_power",
                                "damages": [
                                    "(1 + poison_attack_power * 0.49460351500292177) * (1 + magical_damage_addition) * (1 + skill_damage_final_addition) * (1 + poison_overcome) * (1 - poison_shield * (1 - all_shield_ignore / 1024) / (poison_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + poison_damage_scale)"
                                ]
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
                        32369: {
                            17: {
                                "name": "",
                                "comment": "",
                                "critical_strike": "physical_critical_strike + (300 * recipe_3055_1 + 400 * recipe_3056_1) / 10000",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.03822615516382813 + weapon_damage + rand * weapon_damage_rand) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * 0.03822615516382813) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
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
                                "critical_strike": "physical_critical_strike",
                                "critical_power": "physical_critical_power",
                                "damages": [
                                    "(1 + physical_attack_power * int(152.66772674999999 * (1.0 + 0.2 * buff_34489_1)) * 0.0001737552507446733) * (1 + physical_damage_addition) * (1 + skill_damage_final_addition) * (1 + physical_overcome) * (1 - physical_shield * (1 - all_shield_ignore / 1024) / (physical_shield * (1 - all_shield_ignore / 1024) + shield_constant)) * (1 - (level - 50) * 0.05) * (1 + strain) * (1 + pve_damage_addition) * (1 + physical_damage_scale)"
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}
