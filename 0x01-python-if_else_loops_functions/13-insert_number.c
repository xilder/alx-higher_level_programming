#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a node into a sorted singly linked list.
 * @head - start of the singly linked list
 * @number - value to be added
 * Return: NULL if the function fails or pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while(current->next && current->next->n < new->n)
		current = current->next;
	new->next = current->next;
	current->next = new;
	
	return(new);
}
