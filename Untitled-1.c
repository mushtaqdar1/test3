PROGRAM:
#include <stdio.h>
#incl ude<stdlib.h> 
void main()
{
char str[]="Hello World"; char
str1[11];
char str2[11]=str[]; int i,len;
len = strlen(str);
for(i=0;i<len;i++)
{
str1[i] = str[i]&127;
printf("%c",str1[i]);
}
printf("\n");
for(i=0;i<len;i++)
{
str3[i]=str2[i]^127;
printf("%c",str3[i]);
}
printf("\n");
}
OUTPUT :Hello
World
Hello World
Hello World
Output:
