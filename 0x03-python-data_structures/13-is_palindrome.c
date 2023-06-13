#include "lists.h"

/**
 * is_palindrome - check if a singly list is a palindrome
 * @head: pointer to pointer to listint_t
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *compare = *head;
	unsigned int i, count_c = 0, count;
	float sum2 = 0, sum = 0;

	for (i = 0; compare != NULL; i++)
	{
		count_c++;
		sum += compare->next != NULL ? (compare->n * compare->next->n): 0;
		compare = compare->next;
	}
	count = count_c / 2;
	for (i = 0; i < count; i++)
	{
		sum2 += (current->n * current->next->n);
		current = current->next;
	}
	if ((count_c % 2) == 0 && count_c != 0)
		sum2 -= ((float)(current->n * current->n)) / 2;
	if ((sum / 2) != sum2)
		return (0);
	return (1);
}
