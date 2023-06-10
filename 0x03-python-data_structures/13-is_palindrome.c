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
	int i, j, count_c = 1;

	current = *head;
	compare = *head;
	if (current == NULL)
		return (1);

	for (i = 0; compare != NULL; i++)
	{
		current = *head;
		for (j = 0; (current != NULL && j < count_c); j++)
		{
			if (!i)
				count_c++;
			current = current->next;
		}
		if (current == NULL)
			count_c = j - 1;
		if (current != NULL)
		{
			if (compare->n != current->n)
				return (0);
			count_c--;
			compare = compare->next;
		}
	}

	return (1);
}
