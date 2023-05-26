const screenWidth = window.innerWidth
console.log(screenWidth)

function onSmallScreen(){
    try{
        const card_names = document.querySelectorAll('.place_name')
        if(screenWidth <= 500){
            for(i=0; i<card_names.length; i++){
                card_names[i].classList.add('truncateTitle')
            }
        }
    }
    catch{

    }
}