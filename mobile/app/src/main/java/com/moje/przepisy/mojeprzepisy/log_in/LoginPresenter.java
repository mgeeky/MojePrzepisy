package com.moje.przepisy.mojeprzepisy.log_in;

import com.moje.przepisy.mojeprzepisy.data.ui.utils.repositories.UserRepository;

public class LoginPresenter implements LoginContract.Presenter, UserRepository.OnLoginFinishedListener {

  private UserRepository userRepository;
  private LoginContract.View loginView;

  public LoginPresenter(LoginContract.View loginView, UserRepository userRepository) {
    this.loginView = loginView;
    this.userRepository = userRepository;
  }

  @Override
  public void validateCredentials(final String login, String password) {
    if(loginView != null) {
      userRepository.login(login, password, this);
    }
  }

  @Override
  public void onDestroy() {
    loginView = null;
  }

  @Override
  public void onLoginAndPasswordError() {
    if(loginView != null) {
      loginView.showLoginAndPasswordError();
    }
  }

  @Override
  public void onSuccess() {
    if(loginView != null) {
      loginView.navigateToMainRegisteredActivity();
    }
  }
}