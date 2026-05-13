% Slot antenna on infinite ground plane
% Principal-plane patterns for:
%   aperture size a = 1.5*lambda, b = 2*lambda
%   E_tan = y_hat * E0 * cos(pi*x/a)
%
% E-plane: yz plane, phi = 90 deg
% H-plane: xz plane, phi = 0 deg

clear; clc; close all;

lambda = 1;
a = 1.5 * lambda;
b = 2.0 * lambda;
k = 2 * pi / lambda;

theta_deg = -90:0.1:90;
theta = deg2rad(theta_deg);

% -------- E-plane pattern: phi = 90 deg --------
uE = (k * b / 2) * sin(theta);
FE = abs(sinc_local(uE));
FE = FE / max(FE);
FE_dB = 20 * log10(FE + eps);
FE_dB = max(FE_dB, -60);

% -------- H-plane pattern: phi = 0 deg --------
q = (k * a / pi) * sin(theta);      % q = 2a/lambda * sin(theta) = 3*sin(theta)
Ix_norm = zeros(size(theta));

regular = abs(1 - q.^2) > 1e-8;
Ix_norm(regular) = cos((k * a / 2) * sin(theta(regular))) ./ (1 - q(regular).^2);

% Removable singularity at q = +/-1
Ix_norm(~regular) = pi / 4;

FH = abs(cos(theta) .* Ix_norm);
FH = FH / max(FH);
FH_dB = 20 * log10(FH + eps);
FH_dB = max(FH_dB, -60);

% -------- Plot --------
figure('Color', 'w');

subplot(2,1,1);
plot(theta_deg, FE_dB, 'b', 'LineWidth', 1.6);
grid on;
xlim([-90 90]);
ylim([-60 0]);
xlabel('\theta (deg)');
ylabel('Normalized Pattern (dB)');
title('E-plane Pattern (\phi = 90^\circ)');

subplot(2,1,2);
plot(theta_deg, FH_dB, 'r', 'LineWidth', 1.6);
grid on;
xlim([-90 90]);
ylim([-60 0]);
xlabel('\theta (deg)');
ylabel('Normalized Pattern (dB)');
title('H-plane Pattern (\phi = 0^\circ)');

sgtitle('Slot Antenna on Infinite Ground Plane');

function y = sinc_local(x)
    y = ones(size(x));
    nz = abs(x) > 1e-12;
    y(nz) = sin(x(nz)) ./ x(nz);
end
