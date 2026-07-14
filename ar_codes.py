# Individual Lap Modifier Enabler [Ralf]
# With an added null check: in the menus the course data pointer is null and
# the original code crashed reading the course id from it.
lap_modifier = [
    0x04005420, 0x807D0004,  # lwz r3, 4(r29)     course data pointer
    0x04005424, 0x28030000,  # cmplwi r3, 0       no course loaded?
    0x04005428, 0x41820030,  # beq exit
    0x0400542C, 0x88030019,  # lbz r0, 0x19(r3)   course id
    0x04005430, 0x28000020,
    0x04005434, 0x40810024,
    0x04005438, 0x28000034,
    0x0400543C, 0x4080001C,
    0x04005440, 0x3C808000,
    0x04005444, 0x6084543F,  # lap table base (entries at 0x80005460+)
    0x04005448, 0x7C0400AE,
    0x0400544C, 0x28000000,
    0x04005450, 0x41820008,
    0x04005454, 0x98030018,  # stb r0, 0x18(r3)   total laps
    0x04005458, 0x4818274C,  # exit: back to 0x80187BA4
    0x04187BA0, 0x4BE7D880,
]

# Enable Staff Ghosts [Ralf] + Unlock Everything
unlock_everything = [
    0x043BC1C4, 0xFFFFFFFF,
    0x041CD680, 0x60000000,
    0x041CDD68, 0x60000000,
]

# Grand Prix Mode: Allow Course Selection [Ralf]
gp_course_selection = [
    0x04169E94, 0x41820050,
]

# Red & Green Fireball Item Limit [Ralf]
fireball_limit = [
    0x0435567C, 0x00000014,
    0x00355651, 0x00000014,
    0x00355641, 0x00000014,
]

# Bomb item limit [Ralf]
bomb_limit = [
    0x00355640, 0x00000005,
]

# Disable "Wrong Direction" Lakitu [Ralf]
disable_reverse_lakitu = [
    0x04251CB0, 0x60000000,
]
