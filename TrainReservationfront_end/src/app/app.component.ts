import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  alrt = false;
  title = 'trainbooking';
  selectedSeats : any = [];
  seats = [
  {number:1,
  isBooked : false,
isSelected :false},
  {number:2,
    isBooked : false,
  isSelected :false},  
    {number:3,
      isBooked : false,
    isSelected :false}, 
       {number:4,
        isBooked : false,
      isSelected :false},
          {number:5,
          isBooked : false,
        isSelected :false}, 
           {number:6,
            isBooked : true,
          isSelected :false}, 
               {number:7,
              isBooked : false,
            isSelected :false},
                {number:8,
                isBooked : false,
              isSelected :false}, 
                 {number:9,
                  isBooked : false,
                isSelected :false}, ];
                constructor(){

                }
                selected(number : any){
                  console.log( number in this.selectedSeats);
                  let seatin = false
                  for (let ele of this.selectedSeats){
                    if (ele == number){
                      seatin = true
                    }
                  }
                  if (this.selectedSeats.length <7 || seatin)
                  {let isIn = false
                    this.alrt = false
                  for(let ele in this.selectedSeats){
                    if (this.selectedSeats[ele] == number){
                      this.selectedSeats.splice(ele,1);
                      isIn = true

                    }
                  }
                  if (!isIn){
                    this.selectedSeats.push(number);
                  }
                  let index = this.seats.findIndex(seat => seat.number == number)
                  this.seats[index].isSelected = !this.seats[index].isSelected;
                  console.log(this.selectedSeats)}
                  else{
                    this.alrt = true; 
                  }

                }
                book(){
                  console.log(this.selectedSeats);
                  
                }
}
