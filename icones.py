import machine
#define WiFi_Logo_width 60
#define WiFi_Logo_height 36
WiFi_Logo_bits = bytearray(b'0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xFF, 0x07, 0x00, 0x00, 0x00,0x00, 0x00, 0xE0, 0xFF, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0xFF,0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC, 0xFF, 0xFF, 0x00, 0x00, 0x00,0x00, 0x00, 0xFE, 0xFF, 0xFF, 0x01, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF,0xFF, 0x03, 0x00, 0x00, 0x00, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00,0x00, 0xFF, 0xFF, 0xFF, 0x07, 0xC0, 0x83, 0x01, 0x80, 0xFF, 0xFF, 0xFF,0x01, 0x00, 0x07, 0x00, 0xC0, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x0C, 0x00,0xC0, 0xFF, 0xFF, 0x7C, 0x00, 0x60, 0x0C, 0x00, 0xC0, 0x31, 0x46, 0x7C,0xFC, 0x77, 0x08, 0x00, 0xE0, 0x23, 0xC6, 0x3C, 0xFC, 0x67, 0x18, 0x00,0xE0, 0x23, 0xE4, 0x3F, 0x1C, 0x00, 0x18, 0x00, 0xE0, 0x23, 0x60, 0x3C,0x1C, 0x70, 0x18, 0x00, 0xE0, 0x03, 0x60, 0x3C, 0x1C, 0x70, 0x18, 0x00,0xE0, 0x07, 0x60, 0x3C, 0xFC, 0x73, 0x18, 0x00, 0xE0, 0x87, 0x70, 0x3C,0xFC, 0x73, 0x18, 0x00, 0xE0, 0x87, 0x70, 0x3C, 0x1C, 0x70, 0x18, 0x00,0xE0, 0x87, 0x70, 0x3C, 0x1C, 0x70, 0x18, 0x00, 0xE0, 0x8F, 0x71, 0x3C,0x1C, 0x70, 0x18, 0x00, 0xC0, 0xFF, 0xFF, 0x3F, 0x00, 0x00, 0x08, 0x00,0xC0, 0xFF, 0xFF, 0x1F, 0x00, 0x00, 0x0C, 0x00, 0x80, 0xFF, 0xFF, 0x1F,0x00, 0x00, 0x06, 0x00, 0x80, 0xFF, 0xFF, 0x0F, 0x00, 0x00, 0x07, 0x00,0x00, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x00, 0x00, 0xF8, 0xFF, 0xFF,0xFF, 0x7F, 0x00, 0x00, 0x00, 0x00, 0xFE, 0xFF, 0xFF, 0x01, 0x00, 0x00,0x00, 0x00, 0xFC, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0xFF,0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE0, 0xFF, 0x1F, 0x00, 0x00, 0x00,0x00, 0x00, 0x80, 0xFF, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00')

#define logo_co2_width 36
#define logo_co2_height 25
# 'icone_co2_36x36', 36x25px
logo_co2= bytearray(b'0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x03, 0x00, 0x00, 0x00,0xFC, 0x0F, 0x00, 0x00, 0x18, 0xFE, 0x1F, 0x00, 0x00, 0xFF, 0xFF, 0x3F,0x00, 0x80, 0xFF, 0xFF, 0x7F, 0x00, 0xC0, 0xFF, 0xFF, 0x7F, 0x00, 0xC0,0xFF, 0xFF, 0x7F, 0x00, 0xE0, 0xFF, 0xFF, 0x7F, 0x00, 0xE0, 0xFF, 0xFF,0xFF, 0x00, 0xE0, 0xFF, 0xFF, 0x7F, 0x00, 0xE0, 0xE0, 0xE0, 0x70, 0x00, 0x78, 0x60, 0x44, 0xE4, 0x01, 0x7C, 0x4E, 0x4E, 0xE6, 0x03, 0x7E, 0x7E, 0xCE, 0xE3, 0x07, 0x7E, 0x7E, 0xCE, 0xF3, 0x07, 0x7F, 0x4E, 0xCE, 0xF9, 0x0F, 0x7F, 0x44, 0xC4, 0xF8, 0x0F, 0xFF, 0xE0, 0x60, 0xE0, 0x0F, 0xFF, 0xFB, 0xFB, 0xEA, 0x0F, 0xFE, 0xFF, 0xFF, 0xFF, 0x07, 0xFE, 0xFF, 0xFF, 0xFF, 0x07, 0xFC, 0xFF, 0xFF, 0xFF, 0x03, 0xF0, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x10, 0x04, 0x10, 0x00' )

#define logo_temperature_width 16
#define logo_temperature_height 36
logo_temperature = bytearray(b'  0x00, 0x00, 0xC0, 0x00, 0x70, 0x03, 0x10, 0x03, 0x10, 0x02, 0x10, 0x02, 0x10, 0xFB, 0x10, 0x02, 0x10, 0x02, 0x10, 0x02, 0x10, 0x02, 0x10, 0x7A, 0x10, 0x7B, 0x10, 0x02, 0x50, 0x02, 0xD0, 0x02, 0xD0, 0x02, 0xD0, 0x7A, 0x50, 0x22, 0xD0, 0x02, 0xD0, 0x03, 0xD0, 0x02, 0xD0, 0x5A, 0x90, 0x73, 0xD0, 0x02, 0xD0, 0x06, 0xD8, 0x06, 0xEC, 0x0D, 0xF4, 0x0B, 0xF4, 0x0B, 0xF4, 0x0B, 0xEC, 0x0D, 0x4C, 0x06, 0xB8, 0x07, 0xE0, 0x01, 0x00, 0x00' )

#define logo_humidite_width 36
#define logo_humidite_height 37
logo_humidite= bytearray(b'0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x7C, 0x00, 0x00, 0x00, 0x00, 0x6E, 0x00, 0x00, 0x00, 0x00, 0xE7, 0x00, 0x00, 0x00, 0x00, 0xC3, 0x00, 0x00, 0x00, 0x80, 0x83, 0x01, 0x00, 0x00, 0x80, 0x81, 0x01, 0x00, 0x00, 0x80, 0x81, 0x01, 0x00, 0x00, 0x86, 0x83, 0x01, 0x00, 0x00, 0x86, 0xC3, 0x01, 0x00, 0x00, 0x0F, 0xFF, 0x00, 0x00, 0x00, 0x0F, 0x7E, 0x00, 0x00, 0x80, 0x19, 0x28, 0x04, 0x00, 0xC0, 0x39, 0x00, 0x0E, 0x00, 0xC0, 0x30, 0x00, 0x0F, 0x00, 0x60, 0x70, 0x00, 0x1F, 0x00, 0x70, 0xE0, 0x80, 0x1B, 0x00, 0x30, 0xC0, 0x80, 0x39, 0x00, 0x38, 0xC0, 0xC1, 0x71, 0x00, 0x18, 0x80, 0xE1, 0x60, 0x00, 0x18, 0x80, 0x61, 0xE0, 0x00, 0x18, 0x80, 0x71, 0xC0, 0x01, 0x18, 0x80, 0x31, 0x80, 0x01, 0x18, 0xC0, 0x39, 0x80, 0x01, 0x30, 0xC0, 0x18, 0x80, 0x03, 0xF0, 0xF0, 0x18, 0x00, 0x03, 0xE0, 0x7F, 0x18, 0x80, 0x01, 0x80, 0x1F, 0x30, 0x80, 0x01, 0x00, 0x00, 0x30, 0xC0, 0x01, 0x00, 0x00, 0xF0, 0xE0, 0x00, 0x00, 0x00, 0xE0, 0x7F, 0x00, 0x00, 0x00, 0x80, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00' )
#define icone_pa_width 36
#define icone_pa_height 35
icone_pa=bytearray (b'0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x03, 0x00, 0x00, 0x00, 0x0C, 0x16, 0x00, 0x00, 0x00, 0x18, 0x3C, 0x00, 0x00, 0x00, 0xF0, 0x3C, 0x00, 0x00, 0x00, 0xE0, 0x3C, 0x00, 0x00, 0x00, 0xF0, 0x00, 0xFC, 0x00, 0x00, 0xC0, 0x80, 0xFF, 0x07, 0x00, 0x00, 0xE0, 0xB7, 0x1F, 0x00, 0x06, 0x70, 0x23, 0x37, 0x00, 0x2C, 0x98, 0x31, 0x66, 0x00, 0x78, 0xCC, 0x30, 0xCC, 0x00, 0x78, 0xDE, 0x10, 0xEC, 0x01, 0x78, 0xF8, 0x30, 0xFC, 0x03, 0x00, 0xE0, 0xFF, 0x1F, 0x03, 0x00, 0x61, 0xFA, 0x19, 0x02, 0x00, 0x60, 0x30, 0x18, 0x06, 0x80, 0x20, 0x10, 0x18, 0x06, 0x80, 0x21, 0x30, 0x10, 0x06, 0x80, 0x71, 0x71, 0x38, 0x06, 0x80, 0xFF, 0xFF, 0xFF, 0x07, 0x80, 0x60, 0x30, 0x30, 0x06, 0x80, 0x21, 0x30, 0x10, 0x04, 0x80, 0x61, 0x30, 0x18, 0x06, 0x80, 0x61, 0x30, 0x18, 0x06, 0x00, 0x61, 0xFC, 0x19, 0x02, 0x00, 0xE3, 0xFF, 0x1F, 0x03, 0x00, 0xFE, 0x30, 0xFC, 0x01, 0x00, 0xDE, 0x30, 0xCC, 0x01, 0x00, 0x8C, 0x11, 0xCC, 0x00, 0x00, 0x98, 0x31, 0x66, 0x00, 0x00, 0x70, 0x33, 0x3B, 0x00, 0x00, 0xC0, 0xB7, 0x0F, 0x00, 0x00, 0x80, 0xFF, 0x07, 0x00, 0x00, 0x00, 0xB8, 0x00, 0x00')

#define icone_danger_noir_width 36
#define icone_danger_noir_height 31
icone_danger_noir= bytearray(b'0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xf8, 0x00, 0x00, 0x00, 0x01, 0xfc, 0x00, 0x00, 0x00, 0x03, 0x9c, 0x00, 0x00, 0x00, 0x07, 0x0e, 0x00, 0x00, 0x00, 0x06, 0x06, 0x00, 0x00, 0x00, 0x0e, 0x07, 0x00, 0x00, 0x00, 0x0c, 0x03, 0x00, 0x00, 0x00, 0x1c, 0x73, 0x80, 0x00, 0x00, 0x38, 0xf1, 0xc0, 0x00, 0x00, 0x38, 0xf0, 0xc0, 0x00, 0x00, 0x70, 0xf0, 0xe0, 0x00, 0x00, 0x60, 0xf0, 0x60, 0x00, 0x00, 0xe0, 0xf0, 0x70, 0x00, 0x00, 0xc0, 0xf0, 0x38, 0x00, 0x01, 0xc0, 0xf0, 0x18, 0x00, 0x03, 0x80, 0x70, 0x1c, 0x00, 0x03, 0x00, 0x60, 0x0c, 0x00, 0x07, 0x00, 0x60, 0x0e, 0x00, 0x06, 0x00, 0x60, 0x06, 0x00, 0x0e, 0x00, 0x00, 0x07, 0x00, 0x1c, 0x00, 0x00, 0x03, 0x80, 0x18, 0x00, 0x60, 0x01, 0x80, 0x38, 0x00, 0xf0, 0x01, 0xc0, 0x30, 0x00, 0xf0, 0x00, 0xc0, 0x70, 0x00, 0xf0, 0x00, 0xe0, 0x60, 0x00, 0x00, 0x00, 0x60, 0x60, 0x00, 0x00, 0x00, 0x60, 0x7f, 0xff, 0xff, 0xff, 0xe0, 0x3f, 0xff, 0xff, 0xff, 0xc0, 0x0f, 0xff, 0xff, 0xff, 0x00')
#define icone__danger_blanc_width 15
#define icone__danger_blanc_height 13
icone__danger_blanc= bytearray(b'0x80, 0x01, 0x40, 0x01, 0x60, 0x02, 0xA0, 0x02, 0x90, 0x04, 0x98, 0x0C, 0x88, 0x08, 0x8C, 0x10, 0x04, 0x10, 0x82, 0x20, 0x82, 0x60, 0x03, 0x40, 0xFE, 0x3F')
