import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('Status:').click();
  await page.getByRole('heading', { name: 'DevSecOps Python+FastAPI' }).click();
  await page.getByText('Status: Application runs!').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('{ "status": "ok", "service').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('Status: Application runs!').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByRole('button', { name: 'Load Users' }).click();
  await page.getByRole('heading', { name: 'John Doe' }).click();
  await page.getByText('john.doe@example.com').click();
  await page.getByText('30 years').click();
  await page.getByText('admin').click();
  await page.getByRole('heading', { name: 'Jane Smith' }).click();
  await page.locator('html').click();
  await page.getByRole('heading', { name: 'Bob Johnson' }).click();
  await page.getByText('Alice Brown alice.brown@').click();
});