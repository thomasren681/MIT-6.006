import unittest
from short_company      import short_company

tests = (
    (
        (
            ('SRTBOT', 'Try to Relax Inc.'),
            (
                (13, 25, 14, 2, 9, 17, 16, 13, 10, 16),
                (12, 19, 7, 17, 5, 10, 5, 25, 4, 20),
            ),
            5,
            2,
        ),
        (
            'Try to Relax Inc.',
            (19, 17, 10, 5, 4),
        ),
    ),
    (
        (
            ('BitHub', 'GitBucket', 'GitBit'),
            (
                (33, 69, 91, 78, 19, 40, 13, 94, 10, 88, 43, 61, 72, 13, 46, 56, 41, 79, 82, 27, 71, 62, 57, 67, 34, 8, 71, 2, 12, 93),
                (52, 91, 86, 81, 1, 79, 64, 43, 32, 94, 42, 91, 9, 25, 73, 29, 31, 19, 70, 58, 12, 11, 41, 66, 63, 14, 39, 71, 38, 91),
                (16, 71, 43, 70, 27, 78, 71, 76, 37, 57, 12, 77, 50, 41, 74, 31, 38, 24, 25, 24, 5, 79, 85, 34, 61, 9, 12, 87, 97, 17),
            ),
            10,
            3,
        ),
        (
            'GitBucket',
            (91, 86, 81, 79, 64, 43, 42, 25, 19, 12, 11),
        ),
    ),
    (
        (
            ('YouMotion', 'MeTube', 'Stumblr', 'Chirper'),
            (
                (225, 39, 10, 216, 21, 180, 213, 139, 175, 101, 215, 181, 135, 71, 134, 208, 61, 218, 56, 174, 151, 212, 108, 149, 71, 116, 127, 170, 165, 180, 204, 92, 22, 84, 157, 30, 125, 151, 162, 86, 217, 49, 63, 5, 188, 70, 30, 181, 57, 96, 204, 44, 86, 110, 209, 16, 26, 201, 38, 219),
                (179, 57, 12, 210, 147, 163, 137, 155, 175, 19, 7, 32, 163, 49, 156, 213, 148, 31, 101, 24, 95, 214, 30, 10, 156, 6, 50, 48, 184, 32, 123, 54, 187, 205, 16, 174, 6, 140, 109, 159, 26, 214, 67, 18, 57, 19, 166, 78, 90, 112, 47, 16, 129, 120, 11, 153, 26, 180, 101, 52),
                (67, 92, 188, 121, 215, 146, 44, 179, 173, 53, 197, 15, 202, 174, 41, 217, 42, 88, 136, 65, 31, 153, 114, 171, 45, 4, 121, 175, 105, 146, 224, 131, 80, 167, 92, 100, 215, 169, 65, 40, 144, 177, 4, 118, 190, 21, 86, 190, 12, 140, 72, 35, 62, 196, 124, 91, 157, 74, 173, 92),
                (152, 163, 219, 159, 34, 184, 80, 100, 192, 107, 213, 167, 21, 1, 153, 50, 179, 86, 41, 62, 58, 164, 115, 97, 182, 225, 173, 146, 224, 107, 9, 103, 224, 180, 146, 108, 198, 170, 182, 12, 43, 115, 17, 67, 180, 41, 115, 136, 125, 144, 155, 194, 1, 10, 127, 84, 80, 215, 120, 13),
            ),
            15,
            4,
        ),
        (
            'MeTube',
            (175, 163, 156, 148, 101, 95, 50, 48, 32, 16, 6),
        ),
    ),
    (
        (
            ('Integer Foods', 'VaLerdes', 'pyneAple', 'Macrohard', 'Faywair', 'O. J. Morgan Juice', 'CosmosY', 'Digion'),
            (
                (213, 97, 281, 325, 43, 372, 67, 8, 206, 348, 214, 162, 2, 110, 8, 368, 387, 2, 346, 271, 314, 51, 98, 61, 312, 333, 102, 155, 144, 353, 94, 52, 244, 204, 322, 42, 12, 141, 232, 60, 132, 69, 335, 267, 334, 331, 178, 59, 80, 143, 10, 22, 21, 106, 349, 133, 286, 162, 188, 291, 22, 384, 360, 312, 336, 254, 365, 330, 235, 328, 223, 191, 276, 92, 107, 193, 301, 150, 5, 71, 78, 139, 171, 173, 189, 368, 48, 174, 400, 318, 19, 22, 139, 84, 77, 299, 149, 185, 203, 281),
                (67, 151, 59, 245, 375, 123, 25, 158, 92, 268, 374, 37, 155, 207, 169, 154, 213, 56, 51, 288, 247, 243, 173, 176, 64, 246, 60, 359, 255, 219, 20, 155, 172, 377, 352, 80, 86, 321, 290, 193, 328, 45, 34, 44, 102, 384, 114, 32, 198, 5, 51, 202, 285, 266, 149, 230, 251, 300, 366, 348, 112, 217, 43, 189, 113, 134, 300, 398, 86, 221, 99, 184, 59, 33, 360, 15, 270, 232, 386, 347, 104, 61, 255, 204, 132, 107, 329, 22, 111, 320, 75, 54, 102, 235, 194, 186, 280, 78, 54, 306),
                (250, 76, 289, 208, 327, 349, 217, 267, 254, 348, 166, 256, 256, 326, 344, 104, 278, 313, 113, 5, 175, 362, 383, 163, 165, 19, 269, 76, 132, 309, 80, 195, 299, 151, 368, 362, 241, 34, 44, 265, 21, 34, 116, 67, 21, 154, 8, 389, 230, 170, 83, 77, 336, 236, 191, 259, 196, 272, 258, 18, 294, 47, 348, 266, 389, 308, 40, 383, 219, 387, 106, 149, 275, 307, 214, 247, 199, 312, 301, 120, 11, 337, 1, 380, 94, 155, 260, 292, 131, 171, 34, 253, 135, 156, 396, 209, 197, 197, 32, 84),
                (329, 66, 123, 147, 374, 172, 29, 19, 247, 214, 73, 252, 309, 368, 42, 345, 358, 78, 181, 211, 19, 314, 239, 198, 235, 25, 52, 242, 399, 78, 11, 17, 307, 317, 68, 323, 166, 54, 359, 282, 333, 178, 100, 197, 398, 399, 252, 57, 31, 313, 359, 240, 315, 324, 173, 334, 64, 350, 366, 319, 152, 66, 199, 151, 382, 349, 63, 266, 97, 20, 201, 228, 191, 388, 98, 234, 183, 324, 39, 23, 21, 249, 131, 14, 267, 342, 292, 293, 111, 118, 48, 398, 322, 400, 258, 358, 269, 216, 260, 157),
                (59, 75, 219, 290, 217, 44, 54, 213, 33, 51, 213, 397, 80, 376, 16, 229, 221, 352, 214, 16, 255, 167, 370, 130, 41, 181, 37, 63, 184, 355, 16, 177, 179, 92, 6, 119, 188, 37, 306, 74, 107, 2, 105, 338, 345, 375, 64, 383, 4, 151, 189, 354, 13, 310, 120, 73, 96, 233, 58, 245, 177, 363, 133, 67, 15, 107, 186, 172, 243, 150, 152, 284, 326, 168, 95, 304, 42, 53, 274, 298, 158, 81, 193, 76, 65, 115, 162, 261, 125, 122, 387, 95, 150, 191, 215, 340, 24, 68, 308, 11),
                (202, 40, 360, 38, 68, 216, 154, 282, 214, 380, 73, 303, 217, 153, 327, 182, 44, 128, 228, 324, 190, 327, 271, 30, 193, 210, 5, 214, 373, 165, 226, 105, 191, 151, 242, 47, 95, 56, 142, 58, 286, 311, 353, 79, 360, 229, 205, 95, 394, 216, 222, 90, 127, 233, 175, 268, 73, 182, 237, 324, 327, 45, 248, 387, 105, 151, 1, 358, 230, 317, 237, 4, 112, 153, 59, 394, 323, 155, 280, 312, 80, 218, 362, 385, 242, 48, 348, 255, 390, 119, 279, 391, 208, 144, 324, 12, 62, 139, 343, 21),
                (1, 132, 204, 270, 298, 364, 203, 228, 53, 383, 130, 182, 146, 387, 345, 101, 305, 44, 19, 37, 135, 157, 274, 175, 61, 272, 128, 391, 84, 35, 213, 149, 145, 267, 69, 294, 268, 322, 108, 273, 54, 211, 325, 279, 207, 380, 399, 143, 150, 227, 191, 291, 322, 71, 81, 64, 357, 62, 196, 206, 303, 240, 72, 287, 343, 154, 182, 324, 243, 381, 213, 112, 245, 251, 356, 257, 163, 253, 334, 31, 228, 154, 74, 382, 254, 27, 319, 111, 14, 182, 242, 201, 6, 270, 35, 352, 42, 352, 380, 343),
                (203, 4, 185, 22, 60, 318, 2, 139, 328, 359, 150, 373, 117, 73, 385, 294, 148, 98, 54, 223, 236, 367, 170, 197, 87, 170, 216, 332, 352, 223, 76, 230, 363, 76, 269, 162, 67, 107, 96, 228, 179, 200, 219, 252, 200, 374, 113, 101, 225, 105, 301, 364, 26, 199, 18, 120, 325, 44, 96, 187, 30, 381, 327, 347, 89, 120, 313, 153, 314, 45, 361, 263, 385, 146, 395, 181, 211, 235, 28, 324, 357, 265, 341, 333, 281, 377, 221, 298, 233, 251, 131, 361, 244, 111, 173, 137, 22, 23, 27, 84),
            ),
            20,
            5,
        ),
        (
            'Integer Foods',
            (384, 360, 312, 254, 235, 223, 193, 189, 174, 139, 84, 77),
        ),
    ),
    (
        (
            ('Intergy', 'Jomang', 'Blorox', 'Calchemy', 'Mooz', 'Ooof', 'PhaseBook', 'Marketix', 'ComLab', 'Zoogle'),
            (
                (180, 2, 149, 336, 4, 72, 33, 220, 349, 114, 312, 204, 286, 114, 233, 99, 174, 312, 53, 311, 44, 164, 166, 275, 234, 167, 131, 15, 268, 23, 98, 189, 42, 108, 269, 178, 97, 104, 129, 345, 374, 377, 155, 160, 265, 197, 131, 247, 177, 365, 123, 23, 157, 283, 38, 5, 236, 254, 371, 225, 25, 212, 253, 236, 226, 61, 44, 42, 124, 51, 392, 79, 212, 110, 226, 314, 40, 219, 287, 387, 202, 21, 93, 128, 251, 113, 66, 143, 181, 164, 223, 55, 286, 147, 313, 278, 104, 365, 152, 399, 227, 264, 310, 237, 275, 325, 134, 140, 119, 9, 61, 315, 365, 51, 89, 376, 213, 128, 112, 146, 377, 338, 4, 380, 275, 264, 220, 26, 63, 197, 331, 140, 61, 378, 290, 184, 118, 346, 367, 361, 280, 339, 145, 114, 379, 123, 34, 266, 158, 346, 168, 120, 192, 322, 246, 147, 299, 88, 71, 8, 284, 259, 168, 188, 300, 326, 13, 67, 203, 80, 91, 262, 40, 70, 392, 106, 397, 255, 292, 393, 357, 110, 121, 376, 68, 120, 390, 197, 181, 312, 303, 68, 323, 256, 56, 316, 14, 270, 306, 184),
                (251, 234, 159, 7, 113, 285, 335, 84, 339, 254, 378, 247, 280, 161, 361, 41, 133, 71, 310, 206, 361, 98, 163, 150, 197, 31, 107, 20, 162, 372, 383, 128, 176, 226, 343, 372, 338, 337, 116, 134, 177, 344, 84, 157, 9, 183, 294, 277, 30, 375, 323, 78, 181, 12, 252, 322, 32, 13, 124, 24, 7, 116, 335, 168, 35, 32, 177, 340, 217, 70, 111, 230, 223, 73, 184, 160, 91, 333, 169, 373, 383, 210, 196, 5, 210, 136, 274, 273, 377, 352, 361, 237, 389, 22, 290, 63, 210, 200, 88, 2, 257, 71, 319, 339, 264, 376, 359, 76, 41, 169, 122, 91, 127, 12, 87, 381, 351, 288, 87, 368, 41, 219, 307, 54, 318, 322, 235, 364, 77, 315, 309, 21, 130, 175, 378, 376, 193, 14, 321, 19, 255, 46, 184, 150, 344, 78, 235, 121, 260, 183, 84, 377, 386, 208, 173, 139, 253, 202, 8, 160, 272, 148, 282, 241, 18, 396, 273, 293, 283, 135, 352, 20, 234, 203, 370, 62, 207, 178, 254, 27, 11, 140, 379, 18, 131, 349, 349, 298, 360, 398, 149, 352, 391, 107, 391, 271, 265, 175, 198, 129),
                (107, 60, 290, 169, 125, 301, 346, 369, 273, 349, 181, 84, 79, 170, 383, 5, 300, 27, 290, 80, 177, 186, 150, 321, 151, 166, 254, 207, 308, 221, 88, 1, 73, 292, 23, 227, 65, 175, 5, 370, 246, 341, 340, 399, 132, 383, 314, 97, 36, 282, 218, 143, 90, 272, 87, 33, 338, 328, 81, 297, 57, 259, 324, 279, 310, 197, 387, 223, 137, 160, 146, 7, 220, 399, 368, 144, 133, 276, 270, 284, 163, 176, 98, 362, 222, 73, 4, 385, 262, 80, 339, 360, 289, 197, 185, 238, 19, 288, 211, 326, 315, 390, 117, 9, 186, 271, 82, 349, 100, 324, 182, 322, 359, 255, 10, 375, 377, 128, 293, 124, 141, 95, 389, 216, 40, 294, 230, 122, 381, 366, 231, 261, 361, 52, 97, 85, 226, 34, 219, 325, 203, 140, 130, 224, 388, 397, 183, 313, 168, 47, 158, 16, 253, 6, 391, 129, 104, 391, 204, 198, 224, 398, 326, 321, 345, 200, 357, 20, 299, 239, 182, 292, 65, 289, 364, 143, 168, 13, 204, 243, 268, 70, 22, 42, 290, 178, 185, 3, 36, 98, 368, 57, 344, 277, 242, 23, 162, 13, 162, 202),
                (65, 392, 326, 141, 209, 344, 73, 305, 76, 207, 157, 262, 31, 84, 65, 69, 247, 362, 329, 367, 392, 371, 24, 374, 267, 23, 285, 354, 382, 358, 324, 199, 93, 177, 300, 43, 42, 287, 90, 136, 104, 134, 168, 359, 363, 130, 133, 265, 234, 80, 388, 230, 283, 79, 20, 324, 300, 91, 329, 263, 18, 388, 162, 37, 99, 332, 234, 313, 123, 235, 268, 82, 364, 171, 336, 70, 244, 396, 285, 30, 279, 43, 266, 176, 2, 397, 41, 54, 219, 312, 181, 292, 232, 172, 194, 263, 186, 326, 61, 70, 163, 12, 94, 376, 65, 10, 173, 312, 99, 23, 212, 331, 32, 358, 160, 200, 27, 308, 393, 365, 87, 184, 40, 210, 28, 226, 182, 310, 318, 388, 131, 345, 159, 289, 233, 212, 93, 16, 233, 136, 98, 199, 33, 184, 50, 64, 14, 180, 11, 91, 207, 316, 354, 335, 7, 166, 234, 284, 382, 356, 254, 244, 42, 27, 275, 206, 135, 15, 332, 265, 50, 42, 171, 184, 51, 242, 17, 79, 265, 321, 147, 19, 1, 193, 173, 81, 281, 357, 76, 83, 90, 400, 82, 328, 349, 125, 320, 169, 13, 248),
                (321, 348, 204, 23, 116, 124, 326, 145, 169, 88, 122, 181, 116, 84, 216, 238, 187, 290, 71, 198, 290, 395, 7, 84, 299, 3, 352, 200, 368, 89, 77, 10, 13, 166, 262, 2, 20, 25, 398, 58, 294, 314, 76, 399, 79, 345, 195, 14, 215, 224, 291, 352, 171, 365, 127, 71, 187, 262, 111, 274, 205, 38, 67, 209, 290, 338, 180, 50, 221, 224, 126, 242, 196, 116, 203, 123, 331, 247, 204, 298, 36, 130, 142, 270, 191, 278, 12, 310, 314, 400, 243, 122, 142, 21, 313, 165, 201, 321, 55, 274, 25, 74, 366, 201, 14, 394, 216, 375, 202, 222, 54, 366, 236, 310, 237, 83, 87, 175, 243, 211, 82, 303, 146, 391, 258, 58, 189, 177, 74, 322, 184, 393, 243, 323, 266, 386, 28, 101, 132, 91, 371, 299, 167, 152, 195, 325, 22, 150, 283, 221, 18, 350, 211, 138, 193, 373, 107, 178, 69, 68, 57, 314, 183, 85, 16, 221, 296, 204, 238, 39, 329, 364, 363, 349, 40, 399, 218, 279, 372, 284, 71, 87, 79, 107, 85, 117, 16, 269, 70, 253, 183, 320, 377, 148, 367, 172, 351, 61, 210, 396),
                (135, 82, 176, 322, 257, 170, 273, 356, 75, 193, 379, 381, 285, 157, 121, 194, 178, 200, 242, 262, 157, 210, 209, 51, 350, 79, 76, 3, 299, 305, 325, 361, 265, 55, 357, 399, 332, 358, 105, 306, 330, 309, 263, 57, 137, 353, 375, 315, 87, 193, 44, 19, 6, 60, 186, 370, 247, 163, 56, 347, 232, 189, 300, 357, 130, 342, 250, 398, 118, 82, 288, 283, 40, 400, 261, 87, 14, 330, 86, 265, 210, 312, 339, 107, 225, 363, 351, 208, 136, 11, 301, 69, 199, 88, 226, 290, 28, 193, 45, 330, 302, 208, 172, 120, 260, 234, 21, 246, 318, 53, 138, 260, 252, 283, 331, 202, 243, 136, 93, 118, 277, 187, 82, 155, 312, 74, 234, 36, 36, 245, 202, 290, 210, 285, 48, 136, 247, 118, 57, 152, 73, 185, 49, 71, 338, 30, 341, 71, 301, 287, 102, 4, 17, 208, 286, 359, 387, 309, 252, 366, 354, 55, 243, 287, 178, 400, 176, 50, 352, 3, 124, 117, 255, 160, 141, 116, 5, 254, 182, 261, 175, 47, 40, 157, 294, 217, 116, 379, 189, 196, 389, 75, 119, 148, 103, 381, 398, 247, 338, 184),
                (145, 197, 314, 67, 399, 62, 206, 182, 257, 242, 118, 336, 364, 192, 324, 184, 222, 143, 184, 206, 393, 393, 366, 145, 54, 246, 150, 62, 229, 79, 177, 125, 381, 96, 174, 256, 118, 57, 349, 197, 200, 238, 263, 237, 290, 317, 113, 346, 205, 258, 160, 250, 120, 162, 266, 351, 1, 48, 242, 163, 202, 117, 221, 25, 295, 395, 21, 209, 48, 135, 103, 372, 168, 92, 58, 93, 358, 187, 15, 120, 23, 5, 196, 274, 3, 67, 60, 310, 311, 103, 42, 380, 239, 102, 1, 267, 319, 213, 35, 275, 91, 120, 117, 213, 196, 244, 1, 224, 108, 196, 392, 22, 316, 138, 15, 299, 178, 361, 189, 173, 347, 233, 329, 69, 306, 265, 48, 129, 53, 366, 53, 140, 13, 355, 73, 318, 396, 338, 70, 195, 107, 294, 338, 164, 104, 216, 261, 257, 62, 287, 55, 355, 244, 64, 261, 230, 241, 92, 233, 281, 174, 66, 214, 131, 194, 41, 290, 259, 172, 120, 233, 128, 180, 247, 397, 211, 13, 229, 371, 4, 283, 208, 392, 397, 229, 115, 220, 124, 130, 245, 244, 73, 117, 226, 146, 185, 335, 249, 307, 77),
                (268, 351, 45, 97, 154, 266, 324, 345, 63, 31, 80, 176, 19, 172, 319, 83, 393, 240, 200, 348, 97, 211, 255, 99, 86, 201, 25, 396, 174, 390, 350, 267, 97, 371, 168, 94, 266, 278, 365, 305, 299, 223, 78, 325, 353, 317, 253, 340, 293, 110, 307, 226, 17, 125, 250, 310, 163, 285, 375, 101, 1, 23, 32, 69, 125, 227, 346, 313, 115, 339, 351, 56, 388, 265, 218, 331, 325, 147, 350, 174, 253, 351, 99, 84, 191, 286, 183, 368, 225, 201, 225, 340, 163, 240, 35, 76, 113, 387, 59, 385, 80, 202, 238, 363, 277, 108, 189, 361, 24, 11, 208, 107, 45, 212, 300, 292, 211, 277, 108, 325, 3, 343, 70, 272, 330, 251, 159, 195, 279, 276, 34, 41, 310, 375, 253, 386, 8, 105, 215, 316, 388, 185, 160, 43, 382, 12, 393, 123, 315, 15, 302, 263, 189, 79, 239, 133, 57, 304, 229, 143, 113, 196, 197, 382, 260, 174, 117, 303, 136, 46, 23, 80, 162, 321, 300, 289, 249, 33, 270, 246, 223, 164, 198, 374, 13, 60, 223, 311, 341, 69, 390, 73, 16, 61, 362, 221, 127, 17, 323, 140),
                (136, 197, 60, 177, 150, 192, 316, 327, 98, 382, 278, 278, 31, 174, 264, 283, 8, 83, 254, 12, 327, 133, 170, 71, 177, 51, 315, 288, 214, 389, 35, 129, 293, 54, 267, 39, 301, 66, 249, 18, 267, 115, 178, 50, 286, 363, 112, 91, 356, 340, 118, 205, 104, 312, 358, 382, 225, 179, 81, 138, 370, 179, 281, 103, 111, 239, 161, 66, 142, 288, 341, 398, 395, 1, 43, 339, 168, 158, 362, 166, 18, 44, 314, 8, 150, 59, 86, 365, 141, 104, 263, 284, 178, 230, 46, 213, 258, 273, 210, 63, 42, 304, 238, 166, 90, 152, 124, 322, 224, 345, 358, 147, 17, 12, 5, 327, 138, 40, 339, 161, 163, 281, 335, 148, 25, 363, 128, 355, 265, 72, 133, 306, 29, 199, 215, 144, 299, 116, 130, 161, 273, 251, 230, 363, 63, 217, 192, 87, 267, 27, 119, 362, 245, 197, 16, 123, 42, 158, 51, 94, 66, 225, 8, 386, 186, 270, 212, 64, 270, 127, 256, 145, 138, 207, 221, 242, 358, 30, 85, 364, 269, 183, 104, 128, 78, 114, 155, 75, 96, 283, 129, 279, 14, 93, 120, 370, 214, 362, 81, 125),
                (389, 287, 66, 298, 349, 87, 382, 127, 269, 397, 154, 363, 380, 11, 370, 236, 103, 32, 211, 86, 196, 259, 199, 109, 198, 274, 270, 253, 53, 65, 45, 273, 6, 42, 6, 383, 125, 382, 203, 231, 346, 142, 212, 177, 339, 203, 133, 372, 40, 391, 81, 301, 125, 380, 108, 24, 390, 28, 262, 35, 355, 229, 128, 231, 364, 399, 390, 339, 69, 308, 321, 261, 149, 7, 307, 76, 180, 342, 184, 188, 153, 257, 329, 353, 130, 69, 12, 246, 376, 103, 312, 204, 174, 243, 155, 226, 72, 244, 152, 359, 170, 179, 327, 309, 195, 203, 297, 206, 357, 257, 153, 346, 388, 290, 121, 97, 221, 111, 136, 264, 86, 261, 72, 306, 265, 388, 273, 399, 260, 332, 244, 175, 133, 222, 155, 234, 334, 270, 27, 374, 100, 132, 235, 354, 36, 10, 104, 306, 53, 132, 1, 111, 95, 317, 89, 339, 185, 313, 138, 5, 346, 337, 9, 11, 312, 86, 159, 121, 202, 256, 379, 186, 182, 45, 299, 222, 60, 359, 13, 394, 89, 8, 305, 273, 140, 181, 379, 107, 197, 101, 164, 95, 92, 255, 337, 78, 314, 303, 259, 209),
            ),
            20,
            10,
        ),
        (
            'Ooof',
            (399, 358, 353, 347, 300, 288, 283, 261, 210, 208, 199, 193, 172, 138, 136, 93, 82, 74, 57, 49, 30, 4, 3),
        ),
    ),
)

def check(test):
    (C, P, n, k), (c_, S_) = test
    c, S = short_company(C, P, n, k)
    if len(S) != len(S_):       return False    # incorrect length
    for j in range(1, len(S)):
        if S[j] >= S[j - 1]:    return False    # not strictly decreasing
    for i in range(len(C)):                     # get index i of c in C
        if c == C[i]: break
    if (i == len(C)):           return False    # c not found in C
    q = 0
    for j in range(len(P[i])):                  # check if a subsequence
        if P[i][j] == S[q]:     q += 1
        if q == len(S):         return True
    return False

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
