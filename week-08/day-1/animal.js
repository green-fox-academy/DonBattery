"use strict";

/* Animal Farm
Create an Animal constructor function
Every animal has a hunger property, which is a number
Every animal has a thirst property, which is a number
When creating a new animal object these properties are created with the default 5 value
Every animal can eat() which decreases their hunger by one
Every animal can drink() which decreases their thirst by one
Every animal can play() which increases both by one
Create a Farm constructor function
The farm has slots which defines the number of free places for animals
The farm has list of Animals
The farm can breed() which creates a new animal if there's place for it
The farm can slaughter() which removes the least hungry animal
The farm can print reports about their current state:
The farm has 11 living animals we are bankrupt
The farm can progress from day to a new day by calling it's progress() method:
All animals should have their methods called randomly with 50% chance
The farm should call its breed and slaughter method at the end of each day
The farm should print report at the end of each day
Print the number of sheeps
Print "bankrupt" if no animals left
Print "okay" if the number of animals is above zero and under the slot number
Print "full" if the number of animals are at the maximum allowed */

class Animal {

    constructor(species) {
        this.species = species;
        this.hunger = 5;
        this.thirst = 5;
    }

    drink () {
        if (this.thirst > 0) {
            this.thirst--;
        }
    }
    eat () {
        if (this.hunger > 0) {
            this.hunger--;
        }
    }
    play () {
        this.hunger++;
        this.thirst++;
        }
    }

class Farm {

    constructor(stock) {
        this.slots = stock;
        this.animals = []
        for (let i = 0; i < stock; i++) {
            this.animals.push(new Animal('sheep'))
        }
    }

    breed () {
        if (this.animals.length < this.slots) {
            this.animals.push(new Animal('Sheep'));
        }
    }

    slaugter () {
        let min = 999;
        let index = -1;
        for (let i = 0; i < this.animals.length; i++) {
            if (this.animals[i].hunger < min) {
                min = this.animals[i].hunger;
                index = i;
            }
        }
        this.animals.splice(index, 1);
    }

    printReport () {
        if (this.animals.length === 0) {
            console.log('\nThe farm is bankrupt.')
        }
        else {
            console.log('\nThe Farm has ' + this.animals.length + ' living animals.')
        }
        if (this.animals.length === this.slots) {
            console.log('\nThe farm is full!')
        }
    }

    progress () {
        for (let i = 0; i < this.animals.length; i++) { 
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].drink()
            }
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].eat()
            }
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].play()
            }        
        }
        this.breed()
        this.slaugter()
        this.printReport()
    }
}

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');

button.addEventListener("click", function() {SheepFarm.progress()}, false);

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full