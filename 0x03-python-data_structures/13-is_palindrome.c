#include "lists.h"

/**
 *is_palindrome - This checks if a singly linked list is a palindrome
 *@head: pointer to pointer
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    int list[1000000], i = 0, j = 0, k = 0;
    listint_t *temp;

    if (head == NULL || (*head) == NULL)
        return (1);
    temp = *head;
    while (temp)
    {
        list[i] = temp->n;
        i++;
        temp = temp->next;
    }
    i--;

    if (i % 2 != 0)
        k = (i + 1) / 2;
    else
        k = i / 2;

    while (j < k)
    {
        if (list[j] != list[i])
            return (0);
        i--;
        j++;
    }
    return (1);
}
