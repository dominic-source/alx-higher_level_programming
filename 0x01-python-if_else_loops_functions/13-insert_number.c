#include "lists.h"

/**
 * insert_node - inserts node at a particular index
 * @head: the pointer to pointer to head
 * @number: the number to insert at node
 * Return: new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	int i;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	for (i = 0; current != NULL; i++)
	{
		if (i == 0 && number < current->n)
		{
			new->n = number;
			new->next = current;
			*head = new;
			return (new);
		}
		else if (number < current->next->n)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		else if (current->next->next == NULL && number > current->next->n)
		{
			new->n = number;
			new->next = NULL;
			current->next->next = new;
			return (new);
		}
		current = current->next;
	}
	new->n = number;
	new->next = NULL;
	*head = new;
	return (new);
}
