const answerToggle = () => {
    const ansCard = document.getElementById("answer");
    const questionCard = document.getElementById("question");
    const showAnsButton =  document.getElementById("show-intervals-button");
    const ansButtonsArray = document.querySelectorAll(".interval-button");
    const buttons = document.querySelectorAll(".button");
    buttons.forEach((item,index) => {
        console.log(index);
        item.addEventListener("click",()=>{
           ansCard.classList.toggle("toggle");
           questionCard.classList.toggle("toggle");
        });
    });
    ansButtonsArray.forEach((item,index)=>{
        
        item.addEventListener("click",()=>{
            //Add the code to update the intervals in database by passing "index" in the function you're using
        });
    });
}
answerToggle();