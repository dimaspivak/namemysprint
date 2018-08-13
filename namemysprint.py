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

# Cyclists, of course. Compiled by exporting the UCI's 2018 WorldTour roster.
NAMES = ['Ackermann', 'Agnoli', 'Ait', 'Alaphilippe', 'Amador', 'Anacona',
         'Anton', 'Arashiro', 'Arcas', 'Armee', 'Arndt', 'Aru', 'Asgreen',
         'Atapuma', 'Bak', 'Bakelants', 'Barbero', 'Barbier', 'Bardet',
         'Battaglin', 'Bauer', 'Bauhaus', 'Benedetti', 'Bennett',
         'Benoot', 'Beppu', 'Berhane', 'Bernal', 'Bernard', 'Betancur',
         'Bettiol', 'Bevin', 'Bidard', 'Biermans', 'Bilbao', 'Bohli', 'Bole',
         'Bonifazio', 'Bono', 'Bookwalter', 'Boswell', 'Bouwman', 'Brambilla',
         'Breschel', 'Brown', 'Buchmann', 'Burghardt', 'Bystrøm',
         'Campenaerts', 'Canty', 'Capecchi', 'Carapaz', 'Carretero', 'Carthy',
         'Caruso', 'Castroviejo', 'Cataldo', 'Cavagna', 'Cavendish', 'Chaves',
         'Cherel', 'Chernetski', 'Chevrier', 'Cimolai', 'Clarke', 'Colbrelli',
         'Conci', 'Consonni', 'Conti', 'Cosnefroy', 'Craddock', 'Cras',
         'Curvers', 'Davies', 'De Buyst', 'De Gendt', 'de Kort', 'de la Cruz',
         'de la Parte', 'De Marchi', 'De Plus', 'De Tier', 'De Vreese',
         'Debesay', 'Debusschere', 'Declercq', 'Degenkolb', 'Demare', 'Dennis',
         'Denz', 'Devenyns', 'Dibben', 'Didier', 'Dillier', 'Dlamini',
         'Dombrowski', 'Domont', 'Dougall', 'Doull', 'Dowsett', 'Drucker',
         'Dumoulin', 'Dupont', 'Durbridge', 'Duval', 'Edmondson',
         'Eenkhoorn', 'Eg', 'Elissonde', 'Erviti', 'Ewan', 'Fabbro', 'Faria',
         'Felline', 'Fernandez', 'Ferrari', 'Formolo', 'Fraile', 'Frank',
         'Frankiny', 'Frison', 'Froome', 'Fuglsang', 'Gallopin', 'Ganna',
         'Garcia', 'Gasparotto', 'Gastauer', 'Gatto', 'Gaudu', 'Gautier',
         'Gaviria', 'Geniez', 'Geoghegan', 'Gerrans', 'Geschke', 'Gesink',
         'Ghebreigzabhier', 'Gibbons', 'Gilbert', 'Gogl', 'Golas', 'Gonçalves',
         'Greipel', 'Grivko', 'Grmay', 'Groenewegen', 'Grossschartner',
         'Guarnieri', 'Guerreiro', 'Haas', 'Haga', 'Hagen', 'Haig', 'Hamilton',
         'Hansen', 'Haussler', 'Hayman', 'Henao', 'Hepburn', 'Hindley',
         'Hirt', 'Hodeg', 'Hollenstein', 'Houle', 'Howes',
         'Howson', 'Impey', 'Izaguirre', 'Jansen', 'Jauregui',
         'Jungels', 'Juul', 'Kangert', 'Keisse', 'Kelderman', 'Kennaugh',
         'Keukeleire', 'King', 'Kiryienka', 'Kittel', 'Kišerlovski', 'Knees',
         'Knox', 'Kochetkov', 'Konrad', 'Koren', 'Korsæth', 'Kozhatayev',
         'Kragh', 'Kreuziger', 'Kristoff', 'Kruijswijk', 'Kudus', 'Kuss',
         'Kuznetsov', 'Kwiatkowski', 'Küng', 'Ladagnous', 'Laengen',
         'Lambrecht', 'Lammertink', 'Lampaert', 'Landa', 'Langeveld', 'Latour',
         'Lawless', 'Le', 'Leezer', 'Lindeman', 'Lopez', 'Ludvigsson',
         'Lutsenko', 'Machado', 'Madouas', 'Maes', 'Magnusson', 'Majka',
         'Marcato', 'Marczynski', 'Martin', 'Martinelli', 'Martinez',
         'Mas', 'Matthews', 'McCarthy', 'McLay', 'Meintjes', 'Mertz', 'Meyer',
         'Mezgec', 'Modolo', 'Mohoric', 'Molard', 'Mollema', 'Monfort',
         'Montaguti', 'Morabito', 'Moreno', 'Mori', 'Morton', 'Moscon',
         'Mullen', 'Mørkøv', 'Mühlberger', 'Naesen', 'Narvaez', 'Navardauskas',
         'Nibali', 'Nielsen', 'Nieve', 'Nizzolo', 'Novak', "O'connor",
         'Oliveira', 'Olivier', 'Oomen', 'Oss', 'Padun', 'Pantano', 'Pauwels',
         'Pedersen', 'Pedrero', 'Pellizotti', 'Pernsteiner', 'Peters',
         'Petilli', 'Pfingsten', 'Phinney', 'Pibernik', 'Pinot', 'Planckaert',
         'Poels', 'Polanc', 'Politt', 'Poljanski', 'Porte', 'Power', 'Powless',
         'Pozzovivo', 'Preidler', 'Puccio', 'Quintana', 'Rast',
         'Ravasi', 'Reichenbach', 'Reijnen', 'Restrepo', 'Riabushenko',
         'Richeze', 'Roelandts', 'Roglič', 'Rojas', 'Rolland', 'Roosen', 'Rosa',
         'Roson', 'Rosskopf', 'Roux', 'Rowe', 'Sagan', 'Sanchez',
         'Sarreau', 'Schachmann', 'Schillinger', 'Schmidt', 'Schär', 'Scotson',
         'Scully', 'Selig', 'Senechal', 'Sepulveda', 'Serry', 'Shaw', 'Sieberg',
         'Sinkeldam', 'Siutsou', 'Sivakov', 'Skujins', 'Slagter', 'Smit',
         'Soler', 'Stalnov', 'Stannard', 'Stetina', 'Storer', 'Stuyven',
         'Swift', 'Sütterlin', 'Ten', 'Terpstra', 'Teunissen', 'Teuns',
         'Theuns', 'Thomas', 'Thomson', 'Thwaites', 'Tolhoek', 'Trentin',
         'Tusveld', 'Ulissi', 'Uran', 'Valgren', 'Valls', 'Valverde',
         'Van Asbroeck', 'Van Avermaet', 'van Baarle', 'Van der Sande',
         'van Emden', 'van Garderen', 'van Hoecke', 'Van Hooydonck',
         'van Poppel', 'Vandenbergh', 'Vanendert', 'Vanmarcke', 'Ventoso',
         'Vermote', 'Verona', 'Vervaeke', 'Vichot', 'Villella', 'Vincent',
         'Visconti', 'Viviani', 'Vuillermoz', 'Wallays', 'Walscheid', 'Wellens',
         'Wisniowski', 'Woods', 'Wynants', 'Wyss', 'Yates', 'Zabel',
         'Zakarin', 'Zeits', 'Đurasek', 'Špilak', 'Štybar']


def main():
    print("Your next sprint should be called {} {}.".format(
        random.choice(ADJECTIVES).capitalize(),
        random.choice(NAMES)
    ))


if __name__ == '__main__':
    main()
