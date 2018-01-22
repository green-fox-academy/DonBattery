'use strict';

class TennisPlayer {
  
  constructor(pName) {
    this.name = pName;
    this.score = 0;
  }

}

class TennisGame1 {
  
  constructor(p1Name, p2Name) {
    this.p1 = new TennisPlayer(p1Name);
    this.p2 = new TennisPlayer(p2Name);
  }
  
  wonPoint(playerName) {
    if (playerName === this.p1.name) {
      this.p1.score++;
    }
    else {
      this.p2.score++;
    } 
  }
  
  getScore() {
    var symbol;
    if ((this.p1.score < 4 && this.p2.score < 4) && (this.p1.score + this.p2.score < 6)) {
        var phrases = ["Love", "Fifteen", "Thirty", "Forty"];
        symbol = phrases[this.p1.score];
        return (this.p1.score == this.p2.score) ? symbol + "-All" : symbol + "-" + phrases[this.p2.score];
    } else {
        if (this.p1.score == this.p2.score)
            return "Deuce";
        symbol = this.p1.score > this.p2.score ? this.p1.name : this.p2.name;
        return ((this.p1.score - this.p2.score) * (this.p1.score - this.p2.score) == 1) ? "Advantage " + symbol : "Win for " + symbol;
    }
  }

}

if (typeof window === "undefined") {
  module.exports = TennisGame1;
}