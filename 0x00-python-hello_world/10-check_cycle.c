#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the linkedlist
 * @list: the head of the linked list
 * Return: 0, 1 or -1 on error
 */
int check_cycle(listint_t *list)
{
	listint_t *loop1 = list;
	listint_t *loop2 = list;

	if (list == NULL)
		return (0);
	while (loop1 != NULL && loop2 != NULL)
	{
		loop1 = loop1->next;
		loop2 = loop2->next->next;

		if ((long int)loop1 == (long int)loop2)
			return (1);
	}
	return (0);
}
