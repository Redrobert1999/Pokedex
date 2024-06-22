pokemon = [["Bulbasaur", "001", ["Grass", "Poison"], None, "Ivysaur",
                         "A strange seed was planted on its back at birth. "
                         "The plant sprouts and grows with this Pokemon"],
           ["Ivysaur", "002", ["Grass", "Poison"], "Bulbasur", "Venusaur",
                       "When the bulb on its back grows large, it appears "
                       "to lose the ability to stand on its hind legs."],
           ["Venusaur", "003", ["Grass", "Poison"], "Ivysaur", None,
                        "The plant blooms when it is absorbing solar energy. "
                        "It stays on the move to seek sunlight."],
           ["Charmander", "004", ["Fire"], None, "Charmeleon",
                          "Obviously prefers hot places. When it rains, "
                          "steam is said to spout from the tip of its tail."],
           ["Charmeleon", "005", ["Fire"], "Charmander", "Charizard",
                          "When it swings its burning tail, it elevates the "
                          "temperature to unbearably high levels."],
           ["Charizard", "006", ["Fire", "Flying"], "Charmeleon", None,
                         "Spits fire that is hot enough to melt boulders. "
                         "Known to cause forest fires unintentionally."],
           ["Squirtle", "007", ["Water"], None, "Wartortle",
                        "After birth, its back swells and hardens into a shell. "
                        "Powerfully sprays foam from its mouth."],
           ["Wartortle", "008", ["Water"], "Squirtle", "Blastoise",
                         "Often hides in water to stalk unwary prey. "
                         "For swimming fast, it moves its ears to maintain balance."],
           ["Blasroise", "009", ["Water"], "Wartortle", None,
                         "A brutal Pokemon with pressurized water jets on its shell. "
                         "They are used for high speed tackles."],
           ["Caterpie", "010", ["Bug"], None, "Metapod",
                        "Its short feet are tipped with suction pads that "
                        "enable it to tirelessly climb slopes and walls."],
           ["Metapod", "011", ["Bug"], "Caterpie", "Butterfree",
                       "This Pokemon is vulnerable to attack while its shell "
                       "is soft, exposing its weak and tender body."],
           ["Butterfree", "012", ["Bug", "Flying"], "Metapod", None,
                          "In battle, it flaps its wings at high speed to "
                          "release highly toxic dust into the air."],
           ["Weedle", "013", ["Bug", "Poison"], None, "Kakuna",
                      "Often found in forests, eating leaves. It has a sharp "
                      "venomous stinger on its head."],
           ["Kakuna", "014", ["Bug", "Poison"], "Weedle", "Beedrill",
                      "Almost incapable of moving, this POKéMON can only harden "
                      "its shell to protect itself from predators."],
           ["Beedrill", "015", ["Bug," "Poison"], "Kakuna", None,
                        "Flies at high speed and attacks using its large venomous stingers on its forelegs and tail."]]


# Pokemon layout = "Name": [Number, [Type(s)], prev_evo, next_evo, desc]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs_autocorrect(root_node, to_find, index):
    stack = [root_node]
    found = []
    while stack:
        current_node = stack.pop()
        print(f"searching {current_node.value[0]}")
        if to_find in current_node.value[index]:
            found.append(current_node.value)
        if current_node.children != [None, None]:
            stack += current_node.children
    if not found:
        print("No matching Pokemon found.")
    else:
        print("\nMatching Pokemon:")
        for index in range(len(found)):
            print(f"[{index}] {found[index][0]}")
        choice = -1
        while int(choice) not in range(len(found)):
            choice = input("Please select Pokemon using the corresponding number.\n\n")
            if int(choice) in range(len(found)):
                description(found[int(choice)])
                again = input("\nWould you like to make another search?\n"
                              "                   [Y] Yes   [N] No\n\n")
                while again:
                    if again == "Y":
                        auto_or_reg(root_node)
                    elif again == "N":
                        return
                    else:
                        print("Choice not recognized. Please try again.")

                return
            print("Choice not available, please try again.")


def dfs_regular(root_node, to_find, index):
    stack = [root_node]
    found = []
    while stack:
        current_node = stack.pop()
        print(f"searching {current_node.value[0]}")
        if to_find == current_node.value[index]:
            found.append(current_node)
        if current_node.children != [None, None]:
            stack += current_node.children
    if not found:
        print("No matching pokemon found.")
    else:
        for item in found:
            description(item.value)
    again = input("\nWould you like to make another search?\n"
                  "                   [Y] Yes   [N] No\n\n")
    while again:
        if again == "Y":
            auto_or_reg(root_node)
        elif again == "N":
            return
        else:
            print("Choice not recognized. Please try again.")


def build_tree(lst, index=0):
    if index >= len(lst):
        return None
    print(f"adding \"{lst[index][0]}\"")
    root = TreeNode(lst[index])
    root.children += [build_tree(lst, 2 * index + 1)]
    root.children += [build_tree(lst, 2 * index + 2)]
    return root


def description(lst):
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Index: {lst[1]}\nName: {lst[0]}")
    if len(lst[2]) > 1:
        print(f"Types: {lst[2][0]}, {lst[2][1]}")
    else:
        print(f"Type: {lst[2][0]}")
    if lst[3]:
        print(f"Previous evolution: {lst[3]}")
    if lst[4]:
        print(f"Next evolution: {lst[4]}")
    print(f"Description: \n{lst[5]}")
    print("---------------------------------------------------------------------------------------------------------")


def start_up():
    print("Initializing startup...")
    root_node = build_tree(pokemon)
    print("Startup complete.")
    main_menu()
    auto_or_reg(root_node)


def main_menu():
    print("---------------------------------------------------------------------------------------------------------")
    print("\nVer 0.5.1\nWelcome to the Pokedex.")


def auto_or_reg(root_node):
    index = input("\n\nPlease select a search option below and enter the corresponding letter."
                  "\n                   [1] Name    [2] Index   \n\n")
    index = int(index) - 1
    choice = input("\n\nPlease select a if you want autocorrect enabled for this search."
                   "\n                  [Y] Yes         [N] No\n\n")
    index_list = ["Name", "Index", "Type"]
    if choice == "N":
        to_find = input(f"Please type the {index_list[index]} of the pokemon "
                        "\nyou would like information about.\n\n")
        dfs_regular(root_node, to_find, index)

    elif choice == "Y":
        to_find = input(f"Please type the {index_list[index]} of the pokemon "
                        "\nyou would like information about.\n\n")
        dfs_autocorrect(root_node, to_find, index)
    else:
        print("Entry not recognized.")
        auto_or_reg(root_node)


# def test():
#     root_node = build_tree(pokemon)
#     list = [root_node]
#     while list != []:
#         current_node = list.pop()
#         print(current_node.value[0])
#         if current_node.children != [None, None]:
#             list += current_node.children


start_up()
