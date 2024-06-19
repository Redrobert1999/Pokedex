pokemon = [["Bulbasaur", "001", ["Grass", "Poison"], None, "Ivysaur",
                         "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon"],
           ["Ivysaur", "002", ["Grass", "Poison"], "Bulbasur", "Venusaur",
                       "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs."],
           ["Venusaur", "003", ["Grass", "Poison"], "Ivysaur", None,
                        "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight."],
           ["Charmander", "004", ["Fire"], None, "Charmeleon",
                          "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail."],
           ["Charmeleon", "005", ["Fire"], "Charmander", "Charizard",
                          "When it swings its burning tail, it elevates the temperature to unbearably high levels."],
           ["Charizard", "006", ["Fire", "Flying"], "Charmeleon", None,
                         "Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally."],
           ["Squirtle", "007", ["Water"], None, "Wartortle",
                        "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth."],
           ["Wartortle", "008", ["Water"], "Squirtle", "Blastoise",
                         "Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance."],
           ["Blasroise", "009", ["Water"], "Wartortle", None,
                         "A brutal Pokemon with pressurized water jets on its shell. They are used for high speed tackles."],
           ["Caterpie", "010", ["Bug"], None, "Metapod",
                        "Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls."],
           ["Metapod", "011", ["Bug"], "Caterpie", "Butterfree",
                       "This Pokemon is vulnerable to attack while its shell is soft, exposing its weak and tender body."],
           ["Butterfree", "012", ["Bug", "Flying"], "Metapod", None,
                          "In battle, it flaps its wings at high speed to release highly toxic dust into the air."],
           ["Weedle", "013", ["Bug", "Poison"], None, "Kakuna",
                      "Often found in forests, eating leaves. It has a sharp venomous stinger on its head."],
           ["Kakuna", "014", ["Bug", "Poison"], "Weedle", "Beedrill",
                      "Almost incapable of moving, this POKéMON can only harden its shell to protect itself from predators."],
           ["Beedrill", "015", ["Bug," "Poison"], "Kakuna", None,
                        "Flies at high speed and attacks using its large venomous stingers on its forelegs and tail."]]


#Pokemon layout = "Name": [Number, [Type(s)], prev_evo, next_evo, desc]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(list, index = 0):
    if index >= len(list)
        return None
    root = TreeNode(list[index])
    root.children += [build_tree(list, 2 * index + 1)]
    root.children += [build_tree(list, 2 * index + 1)]
    return root
