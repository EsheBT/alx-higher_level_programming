#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check the cycle in the singly linked list
 * @list: arguments input
 * Return: 0 if no cycle or 1 if its a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current =  list;
	listint_t *current1 = list;

	if (list == NULL)
		exit(0);
	while (1)
	{
		if (current == NULL)
			return (0);
		current = current->next;
		current1 = current1->next->next;
		if (current->next == NULL || current1->next->next == NULL)
			return (0);
		else if  (current->next == current1->next->next)
			return (1);
	}
}
