#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list a cycle in it.
 * @list: pointer to the list to be checked
 * Return: 0 if there is no a cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list) 
{
linstint_t *slow, *fast;
if (!list)
return (0);
slow = list;
fast = list->next;
while (fast && slow && fast->next)
{
if (fast == slow)
return (1);
slow = slow->next;
fast = fast->next->next;
}
return (0);
}
