const cards = document.querySelectorAll('.tower-card');

let hasFlippedCard = false;
let lockBoard = false;
var playerCoins = 10; // change later
var amountBet = 10; 
var coinCounter = 1;
var currentCard;
var lose = false;

function flipCard(){
    //if(lockBoard) return;
    
    if(!lockBoard)
    {
        this.classList.add('flip');
        currentCard = this.dataset.framework;
        console.log("currentCard");
        if(currentCard == "coins"){
            amount = 1.15 * coinCounter;
            coinCounter++;
            this.removeEventListener('click', flipCard);
            if (coinCounter == 4){
                console.log("COINS");
                console.log(amount);
                
            }
        }
        else if(currentCard == "bomb"){
            //indicate player has lost
            console.log("BOMBS");
            lockBoard=true;
            unflipCards();
            lose = true;
            
            
        }
    }

        
}
//firstCard.dataset.framework === secondCard.dataset.framework;

//cards.forEach(card=>card.addEventListener('click', flipCard));
//firstCard.classList.remove('flip');

function unflipCards() {
    lockBoard = true;
    
    setTimeout(() => { cards.forEach(card=>card.classList.remove('flip'));
}, 3000);

}

function resetBoard() {
    hasFlippedCard = false;
    lockBoard = false;
    lose = false;
    
    
    //[hasFlippedCard, lockBoard] = [false, false];
    //[firstCard, secondCard] = [null, null];

}

function shuffle() {
    cards.forEach(card => {
        let randomPos = Math.floor((Math.random() * 12));
        card.style.order = randomPos;
    });
};

//cards.forEach(card=>card.addEventListener('click', flipCard));

function playCards(){
    resetBoard();
    shuffle();
    cards.forEach(card=>card.addEventListener('click', flipCard));
  
}

playCards();