#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the linkedlist
 * @list: the head of the linked list
 * Return: 0, 1 or -1 on error
 */
int check_cycle(listint_t *list)
{
	long *items;
	size_t i;
	int j;

	items = malloc(sizeof(long int) * 2);
	if (items == NULL)
		return (-1);
	for (i = 0; list != NULL; i++)
	{
		if (i != 0)
		{
			items = realloc(items, sizeof(long int) * (i + 2));
			if (items == NULL)
				return (-1);
		}
		items[i] = (long int)list;
		items[i + 1] = '\0';
		list = list->next;
		for (j = 0; items[j] != '\0'; j++)
		{
			if (items[j] == (long int)list)
			{
				free(items);
				return (1);
			}
		}
	}
	free(items);
	return (0);
}
