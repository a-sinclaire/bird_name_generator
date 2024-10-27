# Amelia Sinclaire
# Copyright 2024
import argparse
import random

discoverers = ['Amelia', 'Sammy', 'Sasha', 'Ambre', 'Caroline', 'Jenna', 'Theia', 'Matt', 'Ryan Cubis', 'Max', 'Em', 'Willow', 'Hart', 'Kim']
adjectives = ['Splendid', 'Great', 'Beautiful', 'Glossy', 'Bearded', 'Bi-colored', 'Hairy', 'Ice', 'Electric-type']
colors = ['Black', 'Gray', 'White', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Purple', 'Dark', 'Light', 'Bright', 'Rainbow', 'Cyan', 'Cerulean', 'Seafoam', 'Fiery', 'Crimson', 'Blood', 'Brown', 'Dark Brown', 'Rose', 'Rusty', 'Copper', 'Pink', '#FF00FF']
patterns = [('Spot', 'Spotted'), ('Band', 'Banded'), ('Bar', 'Barred'), ('Stripe', 'Striped'), ('Bare', None)]
body_parts = ['Whiskered', 'Faced', 'Footed', 'Fronted', 'Girdled', 'Goggled', 'Hooded', 'Mantled', 'Masked', 'Naped', 'Necked', 'Sided', 'Tipped', 'Bellied', 'Backed', 'Rumped', 'Tailed', 'Winged', 'Breasted', 'Crested', 'Headed', 'Shouldered', 'Throated', 'Legged', 'Ringed', 'Thighed', 'Vented', 'Billed', 'Beaked', 'Browed', 'Eyed', 'Capped', 'Cheeked', 'Chested', 'Chinned', 'Collared', 'Cowled', 'Crowned', 'Eared']
cardinalities = [('East', 'Eastern'), ('West', 'Western'), ('North', 'Northern'), ('South', 'Southern')]
locations = ['American', 'Arctic', 'African', 'European', 'Baltimore', 'Lowell', 'Dracut']
modifiers = ['Fruit', 'Gay', 'Migratory']
biomes = ['Swamp', 'Marsh', 'Tree', 'Field', 'Sea', 'Desert', 'Tundra', 'Ocean', 'Reef', 'Beach', 'Park', 'Backyard']
birds = ['Sparrow', 'Hummingbird', 'Hawk', 'Jay', 'Pigeon', 'Warbler', 'Gull', 'Woodpecker', 'Tit', 'Penguin', 'Grosbeak', 'Cowbird', 'Bird', 'Screecher', 'Owl', 'Donkey-bird', 'Parrot', 'Chickadee', 'Nuthatch', 'Cardinal', 'Crow', 'Raven', 'Blackbird', 'Magpie', 'Junco', 'Phoebe', 'Bluebird', 'Swift', 'Flamingo', 'Sapsucker']

def generate_bird_name():
    bird_name = ''
    # Discoverer
    if random.random() < 0.2:  # 20% bird has a discoverer
        bird_name += f" {random.sample(discoverers, 1)[0]}'s"

    # Adjective
    if random.random() < 0.2:
        bird_name += f' {random.sample(adjectives, 1)[0]}'

    # Color (Pattern) (Body-part)
    if random.random() < 0.2:
        color = f' {random.sample(colors, 1)[0]}'

        # Body Part
        body_part = ''
        if random.random() < 0.2:
            body_part = f'{random.sample(body_parts, 1)[0]}'

        # Pattern
        pattern = ''
        if random.random() < 0.2:
            pattern = f'{random.sample(patterns, 1)[0][body_part == ""]}'
            pattern = '' if (pattern == 'None') else f'-{pattern}'

        if body_part is not None or pattern is not None:
            bird_name += color

        bird_name += pattern
        bird_name += '' if body_part == '' else '-'
        bird_name += body_part
    elif random.random() < 0.2:
        bird_name += f' {random.sample(patterns, 1)[0][0]}-{random.sample(body_parts, 1)[0]}'

    # Cardinality
    cardinality = False
    if random.random() < 0.2:
        cardinality = True

    # Location
    location = False
    if random.random() < 0.2:
        location = True
        if cardinality:
            bird_name += f' {random.sample(cardinalities, 1)[0][0]}'
            bird_name += f'-{random.sample(locations, 1)[0]}'
        else:
            bird_name += f' {random.sample(locations, 1)[0]}'

    if cardinality and not location:
        bird_name += f' {random.sample(cardinalities, 1)[0][1]}'

    # Noun / Biome / Color
    modifier = False
    if random.random() < 0.2:
        bird_name += f' {random.sample(random.sample([modifiers, biomes, colors], 1)[0], 1)[0]}'
        modifier = True

    # Bird
    if modifier:
        return bird_name + f'-{random.sample(birds, 1)[0]}'
    return bird_name + f' {random.sample(birds, 1)[0]}'

def main(args):
    for _ in range(args.number):
        print(generate_bird_name())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number',
                        type=int,
                        default=1,
                        help='Number of bird names to generate (>=1)')
    args = parser.parse_args()
    if args.number < 1:
        raise Exception('Number of bird names to generate must be greater than zero.')

    main(args)
