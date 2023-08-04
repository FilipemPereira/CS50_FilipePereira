#include <stdio.h>

int main(void)
{

    int popSize, endSize, year = 0, borned, passedAway;

    do
    {
        printf("Start size:");
        scanf("%d", &popSize);
    }
    while (popSize < 9);

    do
    {
        printf("End size:");
        scanf("%d", &endSize);
    }
    while (endSize < popSize);

    while (popSize < endSize)
    {
        borned = popSize / 3;
        passedAway = popSize / 4;
        popSize += borned;
        popSize -= passedAway;
        year++;
    }

    printf("Years: %d\n", year);
}
