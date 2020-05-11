from app.cards.enums.suit_values import SuitValue

# TODO : Separate rules from events

default_fuck_you_rules = {
    SuitValue.ace: ('Chin', 'GORGÉE TABARNAK'),
    SuitValue.two: ('Deux drops', 'À prendre (noir) ou à donner (rouge)'),
    SuitValue.three: ('Trois drops', 'À prendre (noir) ou à donner (rouge)'),
    SuitValue.four: ('Quatre drops', 'À prendre (noir) ou à donner (rouge)'),
    SuitValue.five: ('Cinq drops', 'À prendre (noir) ou à donner (rouge)'),
    SuitValue.six: ('Histoire', 'Dans ma valise, catégories, rimes, ...'),
    SuitValue.seven: ('Multiples', '1, 2, 3, 4, 5, 6, fuck you'),
    SuitValue.eight: ('Anti-règle', 'Enlève une règle'),
    SuitValue.nine: ('Je n\'ai jamais', '1-2 rounds de malaises huehuehue'),
    SuitValue.ten: ('Tic', 'Tu remarques en dernier, tu bois'),
    SuitValue.jack: ('Règle', 'Une règle de ton choix à ajouter au jeu'),
    SuitValue.queen: ('Question queen', 'Si une de tes questions est répondue, la personne boit'),
    SuitValue.king: ('King shit', 'Domination totale, ton but est de faire chier'),
    'Notes': 'Idées pour être débiles : tu perds a un jeu, tu cales ton verre'
}
