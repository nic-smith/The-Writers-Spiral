using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

// Register DbContext
builder.Services.AddDbContext<YourDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

// Configure authentication
builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options =>
    {
        options.LoginPath = "/Account/Login"; // Set the login path if needed
        options.AccessDeniedPath = "/Account/AccessDenied"; // Set the access denied path if needed

        // Add these lines to ensure cookies are secure and have the appropriate SameSite setting.
        options.Cookie.SecurePolicy = CookieSecurePolicy.Always; // Ensure cookies are always secure
        options.Cookie.SameSite = SameSiteMode.Lax; // Set SameSite to Lax (or Strict if needed)
    });

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthentication(); // Add this line
app.UseAuthorization();

app.MapRazorPages();

app.Run();
