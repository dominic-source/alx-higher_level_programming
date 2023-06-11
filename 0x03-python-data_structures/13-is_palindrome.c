#include "lists.h"
/**
 * is_palindrome - check if a singly list is a palindrome
 * @head: pointer to pointer to listint_t
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *compare = *head;
	int i, sum2 = 0, count_c = 0, sum = 0, count;

	for (i = 0; compare != NULL; i++)
	{
		count_c++;
		sum += compare->n;
		compare = compare->next;
	}
	count = count_c / 2;
	for (i = 0; i < count; i++)
	{
		sum2 += current->n;
		current = current->next;
	}
	if ((count_c % 2) != 0)
		sum2 += current->n / 2;
	if ((sum / 2) != sum2 && count_c != 2)
		return (0);

	return (1);
}







/**
 * description - a less efficient way of finding a palindrome
 *
 *
 *	listint_t *current;
 *	listint_t *compare;
 *	int i, j, count_c = 1;
 *
 *	compare = *head;
 *	for (i = 0; compare != NULL; i++)
 *	{
 *		current = *head;
 *		for (j = 0; (current != NULL && j < count_c); j++)
 *		{
 *			if (!i)
 *			*				count_c++;
 *		       urrent = current->next;
 *		}
 *		if (!i)
 *			count_c = j - 1;
 *		else if (current != NULL)
 *		{
 *			if (compare->n != current->n)
 *				return (0);
 *			count_c--;
 *			compare = compare->next;
 *		}
 *	}
*/
