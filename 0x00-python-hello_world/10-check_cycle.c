#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 in case of no cycle and 1 at the opposite
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second = NULL;

	first = list;
	second = list;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			while (first != NULL && second != NULL)
			{
				if (first == second)
					return (1);
			}
		}
	}
	return (0);
}