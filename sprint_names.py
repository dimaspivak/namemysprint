#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The entire stupid project."""

import random

# Stolen without shame from Docker's names-generator.go.
ADJECTIVES = ['admiring', 'adoring', 'affectionate', 'agitated', 'amazing',
              'angry', 'awesome', 'blissful', 'boring', 'brave', 'clever',
              'cocky', 'compassionate', 'competent', 'condescending',
              'confident', 'cranky', 'dazzling', 'determined', 'distracted',
              'dreamy', 'eager', 'ecstatic', 'elastic', 'elated', 'elegant',
              'eloquent', 'epic', 'fervent', 'festive', 'flamboyant',
              'focused', 'friendly', 'frosty', 'gallant', 'gifted', 'goofy',
              'gracious', 'happy', 'hardcore', 'heuristic', 'hopeful',
              'hungry', 'infallible', 'inspiring', 'jolly', 'jovial', 'keen',
              'kind', 'laughing', 'loving', 'lucid', 'mystifying', 'modest',
              'musing', 'naughty', 'nervous', 'nifty', 'nostalgic',
              'objective', 'optimistic', 'peaceful', 'pedantic', 'pensive',
              'practical', 'priceless', 'quirky', 'quizzical', 'relaxed',
              'reverent', 'romantic', 'sad', 'serene', 'sharp', 'silly',
              'sleepy', 'stoic', 'stupefied', 'suspicious', 'tender',
              'thirsty', 'trusting', 'unruffled', 'upbeat', 'vibrant',
              'vigilant', 'vigorous', 'wizardly', 'wonderful', 'xenodochial',
              'youthful', 'zealous', 'zen']

# Cyclists, of course.
NAMES = ['Armstrong', 'Basso', 'Boonen', 'Cancellara', 'Cavendish',
         'Contador', 'Danielson', 'Evans', 'Froome', 'Hincapie', 'Horner',
         'Hoy', 'Hushovd', 'Julich', 'Kloden', 'Landis', 'Leipheimer',
         'Merckx', 'Museeuw', "O'Grady", 'Phinney', 'Powers', 'Renshaw',
         'Schleck', 'Thomas', 'Ullrich', 'Uran', 'Valverde', 'VanGarderen',
         'Vaughters', 'Voigt', 'Vos', 'Wiggins', 'Zabel', 'Zabriskie']


def main():
    print("Your next sprint should be called {} {}.".format(
        random.choice(ADJECTIVES).capitalize(),
        random.choice(NAMES)
    ))


if __name__ == '__main__':
    main()
