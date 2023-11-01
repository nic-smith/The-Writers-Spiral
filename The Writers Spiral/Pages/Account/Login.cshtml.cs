using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Collections.Generic;
using System.Security.Claims;
using The_Writers_Spiral.Models;
using Microsoft.EntityFrameworkCore;

namespace The_Writers_Spiral.Pages.Account
{
    public class LoginModel : PageModel
    {
        private readonly YourDbContext _context;

        public LoginModel(YourDbContext context)
        {
            _context = context;
        }

        [BindProperty]
        public User UserInput { get; set; }

        public async Task<IActionResult> OnPostAsync()
        {
            var authenticatedUser = await _context.User
                .FirstOrDefaultAsync(u => u.Email == UserInput.Email && u.Password == UserInput.Password);

            if (authenticatedUser == null)
            {
                ModelState.AddModelError(string.Empty, "Invalid login attempt.");
                return Page();
            }

            var claims = new List<Claim>
            {
                new Claim(ClaimTypes.NameIdentifier, authenticatedUser.UserId.ToString()),
                new Claim(ClaimTypes.Name, authenticatedUser.FirstName ?? ""),
                new Claim(ClaimTypes.Email, authenticatedUser.Email ?? ""),
                new Claim("PenName", authenticatedUser.PenName ?? ""),
                new Claim("UserType", authenticatedUser.UserType ?? ""),
                // Add any other claims you need here
            };

            var claimsIdentity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);
            var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);

            await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, claimsPrincipal);

            return RedirectToPage("/Index"); // Redirect to the home page or any other page.
        }
    }
}
