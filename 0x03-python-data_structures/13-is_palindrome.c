#include "lists.h"

/**
 * is_palindrome - check if a singly list is a palindrome
 * @head: pointer to pointer to listint_t
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *compare;
	int i, j, count = 0, count_c = 0;

	current = *head;
	compare = *head;
	if (current == NULL)
		return (1);
	while (current != NULL)
	{
		count++;
		count_c++;
		current = current->next;
	}

	for (i = 0; i < (count / 2); i++)
	{
		current = *head;
		for (j = 0; j < (count_c - 1); j++)
			current = current->next;
		if (compare->n != current->n)
			return (0);
		count_c--;
		compare = compare->next;
	}

	return (1);
}
