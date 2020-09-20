int[ratings.length] ratingsCount = new int[ratings.length];
for(int i =0; i < ratings.length; i += 1){
    for(int x = 0; x<ratings[i].length; x += 1){
        ratingsCount[x] += ratings[i][x]
    }
}
int min = ratingsCount[0];
int minIndex = 0;
for(int i = 0; i < ratingsCount.length; i += 1){
    if(ratingsCount[i] < min){
        min = ratingsCount[i];
        minIndex = i;
    }
}
return minIndex;