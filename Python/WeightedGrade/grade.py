def letterGrade(g, regular):
    if regular:
        if g >= 97:
            return 'A+'
        elif 97 > g >= 93:
            return 'A'
        elif 93 > g >= 90:
            return 'A-'
        elif 90 > g >= 87:
            return 'B+'
        elif 87 > g >= 83:
            return 'B'
        elif 83 > g >= 80:
            return 'B-'
        elif 80 > g >= 77:
            return 'C+'
        elif 77 > g >= 73:
            return 'C'
        elif 73 > g >= 70:
            return 'C-'
        elif 70 > g >= 67:
            return 'D+'
        elif 67 > g >= 65:
            return 'D'
        elif g < 65:
            return 'F'

