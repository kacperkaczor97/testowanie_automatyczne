# Cucumber/JavaScript

Do przedstawienia wybrałem framework Cucumber który można wykorzystywać w wielu językach. Ja do swojej prezentacji wybrałem JavaScript.

https://cucumber.io/

Aby łatwiej wytłumaczyć działanie Cucumber stworzymy biblioteke, która może dowiedzieć się, czy jest już poniedziałek.

Wykonał Kacper Kaczor S16587

## Instalacja

Do zainstalowanie Cucumber potrzebny jest Node.js

Aby sprawdzić czy poprawnie mamy zainstalowanego Node.js otwieramy terminal i wpisujemy:

```bash
node -v
npm -v
```

Oba te polecenia powinny wypisać numery naszych wersji.

## Tworzymy pusty projekt Cucumber

Tworzymy nowy projekt w Node.js

```bash
mkdir hellocucumber
cd hellocucumber
npm init --yes
```
Dodajemy bibliotekę Cucmber

```bash
npm install --save-dev @cucumber/cucumber
```
Tworzymy package.json i tworzymy sekcje Test
```javasript
{
  "name": "hellocucumber",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "cucumber-js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "cucumber": "^7.0.0"
  }
}
```
Tworzymy strukturę plików:
```bash
mkdir features
mkdir features/step_definitions
```
Utwórz plik o nazwie cucumber.js w katalogu głównym projektu i dodaj następującą zawartość:

```javascript
module.exports = {
  default: `--format-options '{"snippetInterface": "synchronous"}'`
}
```
Utwórz również plik o nazwie features/step_definitions/stepdefs.jsz następującą zawartością:
```javascript
const assert = require('assert');
const { Given, When, Then } = require('@cucumber/cucumber');
```
Tak stworzyliśmy projekt z zainstalowanym Cucumber.

## Sprawdzanie instalacji Cucumber


Aby upewnić się, że wszystko działa poprawnie, uruchom Cucumber.

```bash
# Run via NPM
npm test

# Run standalone
./node_modules/.bin/cucumber-js
```
Powinniśmy zobaczyć wynik

```bash
0 Scenarios
0 steps
0m00.000s
```
To oznacza że, Cucumber nie znalazł niczego do uruchomienia.

## Pisanie Scenariusza

Kiedy robimy programowanie oparte na zachowaniu z użyciem Cucumber, używamy konkretnych przykładów, aby określić co chcemy, aby oprogramowanie robiło. Scenariusze są pisane przed kodem produkcyjnym. Rozpoczynają swoje życie jako specyfikacja wykonywalna . Gdy pojawia się kod produkcyjny, scenariusze odgrywają rolę żywej dokumentacji i automatycznych testów .


W Cucumber przykład nazywa się scenariuszem . Scenariusze są definiowane w ```.feature``` plikach, które są przechowywane w katalogu ```features```

Konkretnym przykładem może być to, że niedziela to nie poniedziałek .

Utwórz pusty plik o nazwie o następującej treści: ```features/is_it_monday_yet.feature```

```javascript
Feature: Is it Monday yet?
  Everybody wants to know when it's Monday

  Scenario: Sunday isn't Monday
    Given today is Sunday
    When I ask whether it's Monday yet
    Then I should be told "Nope"
```

Pierwsza linia tego pliku zaczyna się od słowa kluczowego, ```Feature:``` po którym następuje nazwa. Dobrze jest użyć nazwy podobnej do nazwy pliku.

Druga linia to krótki opis funkcji. Cucumber nie wykonuje tej linii, ponieważ jest to dokumentacja.

Czwarta linia Scenario: ```Sunday is not Monday``` to scenariusz , który jest konkretnym przykładem ilustrującym, jak powinno zachowywać się oprogramowanie.

Ostatnie trzy linie zaczynające się od ```Given```, ```When``` i ```Then``` są kroki naszego scenariusza.

## Scenariusz zgłoszony jako niezdefiniowany

Kiedy mamy scenariusz możemy go uruchomić

```bash
npm test
```
Cucumber mówi nam, że mamy jeden ```undefined``` scenariusz i trzy ```undefined``` kroki. Sugeruje również kilka fragmentów kodu, których możemy użyć do zdefiniowania tych kroków:

```javascript

UUU

Warnings:

1) Scenario: Sunday is not Monday # features/is_it_monday_yet.feature:4
   ? Given today is Sunday
       Undefined. Implement with the following snippet:

         Given('today is Sunday', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });

   ? When I ask whether it's Monday yet
       Undefined. Implement with the following snippet:

         When('I ask whether it\'s Monday yet', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });

   ? Then I should be told "Nope"
       Undefined. Implement with the following snippet:

         Then('I should be told {string}', function (string) {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });


1 Scenario (1 undefined)
3 steps (3 undefined)
0m00.000s
```

Wystarczy skopiować każdy z trzech fragmentów dla niezdefiniowanych kroków i wklej je do:

```features/step_definitions/stepdefs.js```

### Scenariusz zgłoszony jako oczekujący

Po uruchomieniu Cucumber:
```javascript
P--

Warnings:

1) Scenario: Sunday is not Monday # features/is_it_monday_yet.feature:4
   ? Given today is Sunday # features/step_definitions/stepdefs.js:3
       Pending
   - When I ask whether it is Monday yet # features/step_definitions/stepdefs.js:8
   - Then I should be told "Nope" # features/step_definitions/stepdefs.js:13

1 Scenario (1 pending)
3 steps (1 pending, 2 skipped)
0m00.001s
```
Cucumber znalazł nasze definicje kroków i wykonał je. Obecnie są oznaczone jako oczekujące.

## Scenariusz zgłoszony jako niepowodzenie

Kod definicji:

```javascript
const assert = require('assert');
const { Given, When, Then } = require('@cucumber/cucumber');

function isItMonday(today) {
  // We'll leave the implementation blank for now
}

Given('today is Sunday', function () {
  this.today = 'Sunday';
});

When('I ask whether it\'s Monday yet', function () {
  this.actualAnswer = isItMonday(this.today);
});

Then('I should be told {string}', function (expectedAnswer) {
  assert.equal(this.actualAnswer, expectedAnswer);
});
```

Uruchom Cucumber:
```bash
..F

Failures:

1) Scenario: Sunday is not Monday # features/is_it_monday_yet.feature:4
   ✔ Given today is Sunday # features/step_definitions/stepdefs.js:8
   ✔ When I ask whether it's Monday yet # features/step_definitions/stepdefs.js:12
   ✖ Then I should be told "Nope" # features/step_definitions/stepdefs.js:16
       AssertionError [ERR_ASSERTION]: undefined == 'Nope'
           at World.<anonymous> (/private/tmp/tutorial/hellocucumber/features/step_definitions/stepdefs.js:17:10)

1 Scenario (1 failed)
3 steps (1 failed, 2 passed)
```

Pierwsze dwa kroki mijają, ale ostatni kończy się niepowodzeniem.

## Scenariusz zgłoszony jako pozytywny

Zwróć funkcje ```Nope```

```javascript
function isItMonday(today) {
  return 'Nope';
}
```

Uruchom Cucumber:
```bash
...

1 Scenario (1 passed)
3 steps (3 passed)
0m00.003s
```

Tak wygląda podstawowe użycie Scenariusza Cucumber