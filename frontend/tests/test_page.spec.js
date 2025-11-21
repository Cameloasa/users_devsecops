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


test('Health check and load users', async ({ page }) => {
  // Navigate to homepage
  await page.goto('http://127.0.0.1:8000');

  // Click the health check button and verify JSON
  await page.getByRole('button', { name: /Test Health Check/i }).click();
  const healthJson = await page.getByTestId('health-json').textContent();
  expect(healthJson).toContain('"status": "ok"');
  expect(healthJson).toContain('"service": "FastAPI backend"');

  // Click the "Load Users" button
  await page.getByRole('button', { name: /Load Users/i }).click();

  // Verify at least 4 users are displayed
  const userRows = await page.locator('.user-row').count();
  expect(userRows).toBeGreaterThanOrEqual(4);

  // Check specific user data is visible
  await expect(page.getByText(/John Doe/i)).toBeVisible();
  await expect(page.getByText(/Jane Smith/i)).toBeVisible();
  // Add more users as needed, e.g.:
  // await expect(page.getByText(/Alice Johnson/i)).toBeVisible();
  // await expect(page.getByText(/Bob Brown/i)).toBeVisible();
});