# Extra details about the solution code

## Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

## Plot stones on 2D plane

![leetcodej](https://user-images.githubusercontent.com/46225357/116290190-d6842800-a7b0-11eb-84c2-6cce685ba023.png)

## Used i,~j instead of i,j to run code in less time
## In 2d array ~i or ~j starts with -1 and goes on like -1,-2,-3...

![leetcodei](https://user-images.githubusercontent.com/46225357/116290227-e439ad80-a7b0-11eb-83cd-cbbbc58bf3ca.png)

<p>
 0 , -1 Union find with same row or column of the element,<br>
 0 , -2 Union find with same row or column of the element,<br>
 1 , -1 Union find with same row or column of the element,<br>
 1 , -3 Union find with same row or column of the element,<br>
 2 , -2 Union find with same row or column of the element,<br>
 2 , -3 Union find with same row or column of the element,<br>
</p>
