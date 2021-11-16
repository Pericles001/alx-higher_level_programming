#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 in case of no cycle and 1 at the opposite
 */

int check_cycle(listint_t *list)
{
	listint_t *one, *two = NULL;

	one = list;
	two = list;

	while (one && two && two->next)
	{
		one = one->next;
		two = two->next->next;

		if (one == two)
		{
			while (one != NULL && two != NULL)
			{
				if (one == two)
					return (1);
			}
		}
	}
	return (0);
}