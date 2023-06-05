#include "lists.h"

/**
 * check_cycle - checks for availabilty of cycle in link-lists
 * @list: linked list to be checked
 * Return: 1 if cycle is available or 0 if it is not.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
