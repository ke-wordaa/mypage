#include<stdio.h>
#include<stdbool.h>
int main(void)
{
    int in_1=0, in_2=0,a=0,i= 0,sum,or_text;
    bool l =true;
	while(l==true)
	{
		if(in_1==0&&in_2==0)
		{
			if(i!=0)
			{
				printf("\n------------------\n");	
			}
			i+=1;
    		printf("\n兩個數字必須(1-100)不能為負數!!!!\n\n");
    		printf("請輸入兩個數字(中間以空格區隔開):");
    		scanf("%d %d", &in_1,&in_2);
		}
   		if(in_1>0&&in_2>0&&in_1<100&&in_2<100){ 
        	printf("請問要用+(1)or-(0)計算呢?");
        	scanf("%d", &or_text);
        	if (or_text ==  1)
        		{
        			sum= in_1+in_2;
        			if(sum<0||sum>100)
						{
							printf("無法計算!!");
        					l=false;
     						in_1 = 0;
     						in_2 = 0;
        				break; 	       				
						}
            		printf ("%d\n",sum);
        		}	
			else
				{
            		sum= in_1-in_2;
            		if(sum<0||sum>100)
						{
							printf("無法計算!!");
        					l=false;
     						in_1 = 0;
     						in_2 = 0;
							break;        				
						}
            		printf ("%d\n",sum);
        		}
        printf("是否要繼續(1/0):");
        scanf("%d",&a);
     	if (a!=1)
		 	{
     			l=false;
     			in_1 = 0;
     			in_2 = 0;
     			printf("\n謝謝的使用!");
		 	}	
		else
		 	{
		 		in_1 = 0;
     			in_2 = 0;
		 	}      
    	 }
    	else
    		{
        	printf("無法計算!!");
        	l=false;
     		in_1 = 0;
     		in_2 = 0;
    		}	
    }
}