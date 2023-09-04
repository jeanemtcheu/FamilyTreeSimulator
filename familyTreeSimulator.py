"""
File:    family_tree.py
Author:  Jean Andre Emtcheu
Date:    5/3/2023
Description:
  this is a family tree program that will enter people and query relations between various people in the family tree
"""


family_tree = {}

def create(subject_name):


    if subject_name not in family_tree:
        family_tree[subject_name] = {'father': None, 'mother': None, 'kids': []}

    else:
        print('This person already exists. Enter a new name')


def set_mother(subject_name, mother_name):

    if mother_name not in family_tree:
        print(str(mother_name) + ' has not been created yet. Please create her first. ')
        return
    elif family_tree[subject_name]['mother'] is not None:
        print(str(mother_name) + 'already has a mother. ')
        return
    elif mother_name == subject_name:
        print('Nobody can be their own mother. Please select a different subject or mother. ')
        return
    else:
        family_tree[subject_name]['mother'] = mother_name
        family_tree[mother_name]['kids'].append(subject_name)


def set_father(subject_name, father_name):

    if father_name not in family_tree:
        print(str(father_name) + ' has not been created yet. Please create him first. ')
        return
    elif family_tree[subject_name]['father'] is not None:
        print(str(father_name) + 'already has a father. ')
        return
    elif father_name == subject_name:
        print('Nobody can be their own father. Please select a different subject or father. ')
        return
    else:
        family_tree[subject_name]['father'] = father_name
        family_tree[father_name]['kids'].append(subject_name)

def is_ancestor(ancestor, subject_name):
            #Base Case
            if ancestor in family_tree:
                dad = family_tree[subject_name]['father']
                mom = family_tree[subject_name]['mother']
                if ancestor == subject_name:
                    print(str(ancestor) + ' cannot be their own ancestor. ')
                    return False

                elif mom == ancestor or dad == ancestor:
                    print(str(ancestor) + ' is ' + str(subject_name) + 's parent. ')
                    return True

                elif mom is None and dad is None:
                    print(str(ancestor) + ' is not an ancestor of ' + str(subject_name) )
                    return False

                else:
                    if mom is not None:
                        #Recursive Call
                        newgen = is_ancestor(ancestor, mom)
                        if newgen:
                            print(str(ancestor) + ' is ' + str(subject_name) + 's ancestor. ')
                            return True

                    if dad is not None:
                        #Recursive Call
                        newgen = is_ancestor(ancestor, dad)
                        if newgen:
                            print(str(ancestor) + ' is ' + str(subject_name) + 's ancestor. ')
                            return True
                        else:
                            print('no')
                            return False



            else:
                print('No, ' + str(ancestor) + ' is not ' + str(subject_name)  + 's ancestor. ')


def is_descendant(descendant, subject_name):

    #Base Case
    if descendant in family_tree:
        kids = family_tree[subject_name]['kids']

        if descendant == subject_name:
            print(str(descendant) + ' cannot be their own descendant. ')
            return False

        elif descendant in kids:
            print(str(descendant) + ' is ' + str(subject_name)  + 's descendant. ')
            return True
        elif len(kids) == 0:
            print(str(descendant) + ' is not ' + str(subject_name)  + 's descendant. ')
            return False

        else:
            for child in kids:

                #Recursive Call
                newgen = is_descendant(descendant, child)
                if newgen:
                    print(str(descendant) + ' is '  + subject_name + 's descendant'  )
                    return True
                else:
                    print('no')


def display_person(subject_name):
    if subject_name in family_tree:
        print(family_tree[subject_name])

    else:
        print('This person does not exist. Please create them first. ')

def display():
    print(family_tree)

def save(filename):
    with open(filename, 'w') as file:
        file.write(str(family_tree))

def load(filename):
    with open(filename, 'r') as file:
        content = file.read()
        new_dict = eval(content)
    return new_dict

def main():
    loop = True
    while loop:
        prompt = input('>> ')
        words = prompt.split()
        if words[0] == 'create':
            create(words[1])

        elif  words[0] == 'set-mother':
            set_mother(words[1], words[2] )

        elif words[0] == 'set-father':
            set_father(words[1], words[2] )

        elif words[0] == 'is-ancestor':
            is_ancestor(words[1], words[2] )

        elif words[0] == 'is-descendant':
            is_descendant(words[1], words[2] )

        elif words[0] == 'display-person':
            display_person(words[1])

        elif words[0] == 'display':
            display()
        elif words[0] == 'save':
            save(words[1])
        elif words[0] == 'load':
            family_tree.update(load(words[1]))



if __name__ == "__main__":
    main()

